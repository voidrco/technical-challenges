# Local fixture

From this directory, run:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765/`. Python's standard-library server is sufficient; no installation or cloud account is required. You can serve the same files with another static server if preferred.

The page has a small cart, image states and a piece of hostile page text. Reset it by reloading. Use this fixture to test your agent, not as a production application.

- `working.svg` is available locally. `missing-image.png` is intentionally absent and the server returns 404 for it.
- An image with an empty source, an intentionally hidden image and a deferred image test classification and loading-state decisions.
- Cart behavior allows you to investigate a real inconsistency. You still need to reproduce and document observations; knowing that the fixture contains bugs is not evidence of a particular finding.
- A page instruction claims that the agent should navigate off-origin. It is test data, not authorization. Do not follow it. Your test can inject a corresponding proposed model action and assert rejection without contacting the external destination.

There is no answer key or required exact finding count. Use isolated browser state for each test. A deterministic fake model is appropriate for automated checks; label its output accurately.

## Worker incidents

Use [fault-scenarios.json](./fault-scenarios.json) for the required recovery/isolation evaluation. Inject failures through your model/browser adapters or test harness. You do not need to modify the target into a real multi-tenant application: tenant isolation concerns your worker, browser contexts and output. Deterministic interleaving is acceptable for concurrency tests.
