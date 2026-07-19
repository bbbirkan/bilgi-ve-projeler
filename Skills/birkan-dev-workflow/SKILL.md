
### OTOMATİK Öğrenim [2026-06-27]
> Geliştirici iş akışı: kod yaz → black + isort format → manuel CLI testi (python cli.py --help). black/isort entegrasyonu CI öncesi format tutarlılığı sağlar.
>
> Pre-commit hook + GitHub Actions iş akışına 'ruff format --check && ruff check' adımı ekle; her yeni repo'da (channel-watcher, yt-signal vb.) varsayılan şablon olsun.
