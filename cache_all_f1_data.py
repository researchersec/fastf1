import fastf1
import pandas as pd

fastf1.Cache.enable_cache('cache') 

def cache_season_data(season):
    """Cache all sessions for a season."""
    event_schedule = fastf1.get_event_schedule(season)
    for event in event_schedule.itertuples():
        print(f"Fetching data for {event.OfficialEventName} ({event.Country}) - {event.EventDate}")

        for i in range(1, 6): 
            session_name = getattr(event, f'Session{i}')
            session_date = getattr(event, f'Session{i}Date')
            
            if pd.isna(session_name) or pd.isna(session_date):
                continue 

            try:
                print(f"  Caching session: {session_name} on {session_date}")
                session = fastf1.get_session(season, event.RoundNumber, session_name)
                session.load()  
            except Exception as e:
                print(f"    Error caching session {session_name}: {e}")

def main():
    for season in range(2011, 2024):
        print(f"Caching season {season}")
        cache_season_data(season)
    print("All data cached successfully.")

if __name__ == "__main__":
    main()
