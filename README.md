# Instagram Promotion Assistant

A GitHub Actions-based reminder and workflow assistant for an Instagram post.

> This project intentionally does **not** automatically submit requests to third-party
> engagement/likes services. It prepares the task and records the cycle so that the
> actual submission remains manual.

## Workflow

1. GitHub Actions runs on a schedule.
2. The Python script records the current cycle.
3. The configured Instagram post URL is displayed in the workflow log.
4. The operator manually performs any desired promotion.
5. The next scheduled cycle runs.

## Configuration

Edit `config.json`:

```json
{
  "instagram_url": "https://www.instagram.com/p/DcokpCGDHMP/?utm_source=ig_web_copy_link&igsi=MzRlODBiNWFlZA==",
  "promotion_page": "https://zefame.com/en/free-instagram-likes",
  "cooldown_minutes": 32
}
```

## Run locally

```bash
python promotion_assistant.py
```

## GitHub Actions

The workflow is configured to run every 35 minutes. GitHub Actions cron scheduling
is not an exact timer and may be delayed during periods of high GitHub load.

The workflow does not log in to Instagram, bypass protections, or automatically
submit third-party engagement requests.
