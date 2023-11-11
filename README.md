# GPT4-V Initial Experiment

Experimenting with GPT4 Vision Preview model with a use case of figuring getting info about an image in both text and voice (using OpenAI TTS).

## Getting Started

The `server` folder contains the Python code and the `ui` folder contains the SvelteKit code.

### Update `docker-compose.yml` 

Add you OpenAI API key to the `docker-compose.yml` file in the `server` environments.

### Build and Start the servers

Run the following command to start the server and the ui.

```sh
docker-compose up
```

After changing any file, use the following command.

```sh
docker-compose build && docker-compose up
```