FROM	python:3.11

RUN	apt-get update \
		&& apt-get install -y \
			gcc \
			build-essential \
			libatlas-base-dev \
			libblas-dev \
			liblapack-dev \
		&& rm -rf /var/lib/apt/lists/*

RUN	pip install --upgrade pip
RUN	pip install \
		qiskit==2.0.0 \
		matplotlib \
		qiskit[visualization] \
		qiskit-aer==0.17.0 \
		jupyter
RUN	pip install --upgrade qiskit qiskit-aer

WORKDIR	/workspace

COPY	. .

# CMD ["tail", "-f", "/dev/null"]
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--NotebookApp.token=''"]
