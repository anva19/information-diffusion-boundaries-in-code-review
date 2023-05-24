from coverage import Coverage

cov = Coverage()
cov.start()
with open("/home/zeri/information-diffusion-boundaries-in-code-review/test/test_minimal_paths.py") as f:
    exec(f.read())
cov.stop()
cov.save()
cov.json_report("json_report.json")
