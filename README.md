# Launchpad

Launchpad is a production-shaped Flask delivery control room: a responsive dashboard for deployments, service health, team activity, and incidents.

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
flask --app app run --debug
```

Open `http://localhost:5000`. Run the test suite with `pytest -q`.

## Run with Docker

```bash
docker compose up --build
```

The image runs as a non-root user and includes a Docker health check. The Kubernetes bundle in `k8s/launchpad.yaml` includes a namespace, config map, rolling deployment, service, ingress, resource limits, and HTTP probes. 

## CI/CD

`.github/workflows/ci-cd.yml` runs compilation and tests on every pull request, builds and scans a GHCR image on pushes to `main` or version tags, and deploys version tags to Kubernetes. Configure the repository's `KUBE_CONFIG` secret and a `production` environment before enabling the deploy job.