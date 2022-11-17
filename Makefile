run:
	docker build -t wkye/leaving-academia-for-tech .
	docker run --rm --name leaving-academia-for-tech \
	-v /Users/willie/data/leaving-academia-for-tech \
	-p 8888:8888 \
	wkye/leaving-academia-for-tech
