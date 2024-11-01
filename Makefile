 install:
	pip install --upgrade pip  &&\
	pip install -r requirements.txt &&\
	pip install ruff &&\
	pip install nbqa &&\
	pip install nbval &&\
	pip install pytest pytest-cov

format:
	black *.ipynb #format all files	

lint:
	nbqa ruff *.ipynb

test:
	py.test --nbval *.ipynb

generate_and_push:
	git pull	
	git config --local user.email "action@github.com"
	git config --local user.name "GitHub Action"
	git add .
	git commit -m "rerun push" --allow-empty
	git push
