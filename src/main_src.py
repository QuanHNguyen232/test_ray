print("Hello from test-ray/src!")

try:
    import ray
    ray.init()
    print("ray version:", ray.__version__)
    print("cluster_resources:", ray.cluster_resources())
    print("available_resources:", ray.available_resources())    
except Exception as e:
    print("Error initializing Ray:", e)

try:
    import torch
    print("torch version:", torch.__version__)
    print("torch cuda is available:", torch.cuda.is_available())
except Exception as e:
    print("Error importing torch:", e)
    
try:
    import emoji
    print(emoji.emojize("This is a test :thumbs_up:"))
except ImportError:
    print("Emoji library not found. Please install it to see emojis.")
    
@ray.remote
def add_one(a):
    return a + 1
try:
    obj_ref = add_one.remote(0)
    for i in range(1000):
        obj_ref = add_one.remote(obj_ref)
    print(ray.get(obj_ref))
except Exception as e:
    print("Error running Ray remote func:", e)
    

if ray.is_initialized():
    ray.shutdown()