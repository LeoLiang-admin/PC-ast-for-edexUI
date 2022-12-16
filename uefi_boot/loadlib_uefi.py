def load():
    from time import sleep
    from tqdm import tqdm

    print("Loading Lib(.py)")
    for i in tqdm(range(1, 20)):
        sleep(0.01)
    print("successful.")
    print("\nLoading Lib(.png)")
    for i in tqdm(range(1,8)):
        sleep(0.2)
    print("successful.")
    print("\nLoading Lib(files)")
    for i in tqdm(range(1,5)):
        sleep(0.01)
    print("successful.\n\n")