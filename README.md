# Launch Ray job

## Set env variable
```bash
export RAY_API_SERVER_ADDRESS=
```

## 2 methods to launch job
1. Launch job from URI
    ```bash
    ray job submit --no-wait \
        --working-dir https://github.com/QuanHNguyen232/test_ray/archive/HEAD.zip \
        -- uv run --directory src main_src.py
    
    # OR python
    ray job submit --no-wait \
        --working-dir https://github.com/QuanHNguyen232/test_ray/archive/HEAD.zip \
        --runtime-env-json='{"pip": "./src/requirements.txt"}' \
        -- python src/main_src.py
    ```

1. Launching job from local
    ```bash
    git clone https://github.com/QuanHNguyen232/test_ray.git
    cd test_ray/src

    # install dependencies
    uv sync
    # OR
    pip install -r requirements.txt

    # back to test_ray/
    cd ..

    # using uv
    ray job submit --no-wait --working-dir . -- uv run --directory src main_src.py
    # OR using python
    ray job submit --no-wait --working-dir . --runtime-env-json='{"pip": "./src/requirements.txt"}' -- python src/main_src.py
    ```