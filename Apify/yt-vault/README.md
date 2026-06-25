# YT-Vault

Apify üzerinden YouTube kanallarının tüm video listesini çeker.
Ücretsiz Apify planında çalışır (~0.001 compute unit / kanal).

## Kullanım

```bash
source /root/.sovereign_env
python3 fetch_channel.py "@GrahamStephan"
python3 fetch_channel.py "@GrahamStephan" --max 1000
python3 fetch_channel.py "https://youtube.com/@MeetKevin" --output /root/data
```

## Çıktı

`output/@KANAL_videos.json` — her video için:
- title, url, id
- date, duration, viewCount, likes
- description (ilk 300 karakter)
- channelName, channelTotalVideos

## Sonraki Adım

Transkript çekimi: `fetch_transcripts.py` (ileride)
