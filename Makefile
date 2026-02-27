.PHONY: api worker dev

api:
	uvicorn main:app --reload

worker:
	celery -A worker:celery_app worker --loglevel=info

dev:
	make -j2 api worker