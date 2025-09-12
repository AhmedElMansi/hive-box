# HiveBox App

This is the initial version of the **HiveBox** app.  

---

## Phase 1

- Use **Semantic Versioning** `v0.0.1` for the initial release.  
- Create a function that prints the current app version.  
- The app should simply print the version and then exit.

---

## Containers

Build the Docker image
```bash
docker build -t hivebox:0.0.1 .
```
Run the container
```
docker run hivebox:0.0.1
```
Expected output
```
HiveBox v0.0.1
```