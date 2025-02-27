from googleapiclient.discovery import build

def get_youtubers():
    api_key = 'API_KEY'  # Replace with your YouTube Data API v3 key
    youtube = build('youtube', 'v3', developerKey=api_key)

    query = 'coding'
    min_subscribers = 10000
    max_subscribers = 15000
    max_results = 50  # Maximum number of results per page (up to 50)
    
    search_response = youtube.search().list(
        q=query,
        type='channel',
        part='snippet',
        maxResults=max_results
    ).execute()

    channels = []
    
    for item in search_response['items']:
        channel_id = item['snippet']['channelId']
        channel_title = item['snippet']['title']

        # Get channel statistics
        channel_response = youtube.channels().list(
            part='statistics',
            id=channel_id
        ).execute()

        for channel in channel_response['items']:
            subscriber_count = int(channel['statistics']['subscriberCount'])

            if subscriber_count >= min_subscribers and subscriber_count <= max_subscribers:
                channels.append({
                    'title': channel_title,
                    'id': channel_id,
                    'subscribers': subscriber_count
                })

    return channels

# Example usage
youtubers = get_youtubers()

for youtuber in youtubers:
    print(f"Channel: {youtuber['title']}, Subscribers: {youtuber['subscribers']}")
