### A simple implementation of the [OpenAI Chat Completion](https://platform.openai.com/docs/guides/gpt/chat-completions-api) API built with [FastAPI](https://fastapi.tiangolo.com/)

- The API demo can be found [here](https://www.loom.com/share/7b56de39016546cf964e663c99d5006e?sid=5217093a-8a9a-4922-879e-2f264937b419)

- **DATA-SOURCE** : [huggingface](https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/blob/main/ShareGPT_V3_unfiltered_cleaned_split.json) (Be sure to download the file to the root of the project for the application to work)

### Benchmarks

> As observed, The improvement in performance of the `/api/v1/chat/completion/v1` endpoint is due to the fact that the api uses python [generators](https://realpython.com/introduction-to-python-generators/) to load the dataset on demand, as opposed to loading it all at once hence reducing the memory footprint of the application. It also leverages [redis](https://redis.io) as a caching layer to reduce the number of lookups made to the dataset for repeated payloads.

- NB: these benchmarks might vary due to network conditions and the resource on the machine at the time of testing.

100 Epochs(Requests)

> The sample data in the `benchmark.json` file is extracted from the last 100 dictionaries in the core `ShareGPT_V3_unfiltered_cleaned_split.json` dataset.

`/api/v1/chat/completion` **POST** (with repeated payloads)

```json
{
  "requests_per_minute": "343.76",
  "avg_latency_in_seconds": "0.174539"
}
```

`/api/v1/chat/completion` **POST** (with non-repeated payloads)

```json
{
  "requests_per_minute": "437.89",
  "avg_latency_in_seconds": "0.137020"
}
```

`/api/v1/chat/completion/v1` **POST** (with repeated payloads)

```json
{
  "requests_per_minute": "8079.54",
  "avg_latency_in_seconds": "0.007426"
}
```

`/api/v1/chat/completion/v1` **POST** (with non-repeated payloads)

```json
{
  "requests_per_minute": "3483.11",
  "avg_latency_in_seconds": "0.017226"
}
```

Test Configuration: Macbook Pro 2018, 2.7GHz Quad-Core Intel Core i7, 16GB RAM 2133 MHz LPDDR3 Python 3.9.6

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
