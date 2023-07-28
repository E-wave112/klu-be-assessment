### A simple implementation of the  [OpenAI Chat Completion](https://platform.openai.com/docs/guides/gpt/chat-completions-api) API built with [FastAPI](https://fastapi.tiangolo.com/) 

* The API demo can be found [here](https://www.loom.com/share/5e1ba34ea2ac4f3694e54376f8f4104d?sid=f93b6795-357f-48cc-92b3-9178262de767)

* **DATA-SOURCE** : [huggingface](https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/blob/main/ShareGPT_V3_unfiltered_cleaned_split.json) (Be sure to download the file to the root of the project for the application to work)

### Benchmarks
- NB: these benchmarks might vary due to network conditions and the resource on the machine at the time of testing.

100 Epochs(Requests)

`/api/v1/chat/completion` **POST**

```json
{
  "requests_per_minute": 353.93162027871574,
  "avg_latency": 0.16952427124977112
}
```

`/api/v1/chat/completion/v1` **POST**

```json
{
  "requests_per_minute": 369.69376208443566,
  "avg_latency_in_seconds": 0.1468085641860962
}
```

Test Configuration: Macbook Pro 2018, 2.7GHz Quad-Core Intel Core i7, 8GB 2133 MHz LPDDR3 16GB RAM Python 3.9.6

The improvement in performance of the `/api/v1/chat/completion/v1` endpoint is due to the fact that the api uses python generators to load the dataset on demand, as opposed to loading it all at once hence reducing the memory footprint of the application.


### Getting Started

To get started with the project, ensure you have setup and activated a virtual environment, guides on that [here](https://realpython.com/python-virtual-environments-a-primer/)

clone the repository via the command



```
$ git clone https://github.com/E-wave112/klu-be-assessment
```

install dependencies

```
$ python3 -m pip install -r requirements.txt
```

### Running the development Server

start the server by running the bash script below:
```
$ bash start.sh
```

Alternatively, you can start the server using the command below:
```
$ uvicorn application:app --port 8000 --reload
```

the server will be running on http://localhost:8000/docs