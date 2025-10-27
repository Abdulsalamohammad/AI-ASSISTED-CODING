import os
import sys
import json
import time
import argparse
import getpass
from pathlib import Path
from typing import Optional, Dict, Any
import requests

OPENWEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
ENV_VAR_NAME = "OPENWEATHER_API_KEY"
DOTENV_FILENAME = ".env"

def _parse_local_dotenv(dotenv_path: Path) -> Dict[str, str]:
    env: Dict[str, str] = {}
    if not dotenv_path.exists():
        return env
    for line in dotenv_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip().strip('"').strip("'")
    return env

def _ensure_api_key_interactive(dotenv_path: Path) -> Optional[str]:
    print(f"[!] {ENV_VAR_NAME} not found. Enter your OpenWeather API key (input hidden).")
    api_key = getpass.getpass("API key: ").strip()
    if not api_key:
        return None
    choice = input("Save this key to .env for future runs? [y/N]: ").strip().lower()
    if choice == "y":
        env = _parse_local_dotenv(dotenv_path)
        env[ENV_VAR_NAME] = api_key
        lines = [f"{k}={env[k]}" for k in env]
        dotenv_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"[✓] Saved to {dotenv_path} (remember to add it to .gitignore).")
    os.environ[ENV_VAR_NAME] = api_key
    return api_key

def load_api_key() -> Optional[str]:
    api_key = os.getenv(ENV_VAR_NAME)
    if api_key:
        return api_key.strip()
    script_dir = Path(__file__).resolve().parent
    candidates = [script_dir / DOTENV_FILENAME, Path.cwd() / DOTENV_FILENAME]
    for p in candidates:
        env = _parse_local_dotenv(p)
        if ENV_VAR_NAME in env:
            os.environ[ENV_VAR_NAME] = env[ENV_VAR_NAME].strip()
            return env[ENV_VAR_NAME].strip()
    return _ensure_api_key_interactive(candidates[0])

def fetch_weather(city: str, units: str = "metric", timeout: float = 8.0) -> Dict[str, Any]:
    api_key = load_api_key()
    if not api_key:
        return {"error": f"{ENV_VAR_NAME} missing. Cannot proceed."}
    params = {"q": city, "appid": api_key, "units": units}
    try:
        resp = requests.get(OPENWEATHER_ENDPOINT, params=params, timeout=timeout)
        if resp.status_code == 200:
            payload = resp.json()
            return {"data": {
                "city": payload.get("name", city),
                "country": payload.get("sys", {}).get("country"),
                "temperature": payload.get("main", {}).get("temp"),
                "feels_like": payload.get("main", {}).get("feels_like"),
                "humidity": payload.get("main", {}).get("humidity"),
                "pressure": payload.get("main", {}).get("pressure"),
                "wind_speed": payload.get("wind", {}).get("speed"),
                "weather": (payload.get("weather") or [{}])[0].get("description"),
                "units": units,
            }}
        elif resp.status_code == 401:
            return {"error": "Unauthorized. Check your API key (401)."}
        elif resp.status_code == 404:
            return {"error": f"City '{city}' not found (404)."}
        else:
            return {"error": f"OpenWeather error {resp.status_code}", "detail": resp.text}
    except requests.Timeout:
        return {"error": "Request timed out."}
    except requests.RequestException as e:
        return {"error": f"Network error: {e}"}

def main():
    parser = argparse.ArgumentParser(description="Fetch weather securely.")
    parser.add_argument("city", nargs="?", help="City name (e.g., 'Delhi')")
    parser.add_argument("--units", choices=["standard", "metric", "imperial"], default="metric")
    parser.add_argument("--json", action="store_true", help="Print raw JSON output")
    args = parser.parse_args()

    # If no city was passed, ask interactively
    city = args.city or input("Enter the city name: ").strip()

    result = fetch_weather(city, units=args.units)
    if "error" in result:
        print(f"[x] {result['error']}")
        if "detail" in result:
            print(result["detail"])
        sys.exit(1)

    data = result["data"]
    if args.json:
        print(json.dumps(data, indent=2))
    else:
        city_line = f"{data['city']}" + (f", {data['country']}" if data.get("country") else "")
        print(f"Weather in {city_line}:")
        print(f"  Description : {data.get('weather')}")
        print(f"  Temperature : {data.get('temperature')}° ({args.units})")
        print(f"  Feels like  : {data.get('feels_like')}°")
        print(f"  Humidity    : {data.get('humidity')}%")
        print(f"  Pressure    : {data.get('pressure')} hPa")
        print(f"  Wind speed  : {data.get('wind_speed')}")

if __name__ == "__main__":
    main()
