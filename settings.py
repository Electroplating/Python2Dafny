# settings for LLM
# api_key = "sk-OlSvN7YeLLJi6OUjD1255aBf50F14e6286D1B1911fCc6f97"
# base_url = "https://www.gptapi.us/v1/chat/completions"
# api_key = "sk-9Eyah6sAVyfVvHBXxNth4tMIKVBIlDSd2uPV3NBIbMLhcOzC"
# base_url = "https://api.chatanywhere.tech"
api_key = "sk-MN1dkNfJ09JCbsO6YyLbDmcT3GKLDLxdgjI2LuZKS8SLdJwX"
base_url = "https://us.ifopen.ai/v1"
model = "gpt-4o"
temperature = 0.5
# api_key = "sk-a989ba76e91b4d4ab632685cc5d7a476"
# base_url = "https://api.deepseek.com"
# model = "deepseek-chat"
# temperature = 0.0

max_concurrent_threads = 5

source_code_json_path = "mbpp_code.json"  # Python source code for generating Dafny translations and testcases
dafny_code_path = (
    "mbpp_paths.json"  # The path of JSON file that contains Dafny translation paths
)
test_set_json_path = "mbpp_test.json"  # Testcases for evaluating Dafny translations
translation_path = "mbpp_code_gen"  # Path for generated translations
test_set_generation_json_path = "generated_test.json"  # LLM Genarated testcases

# settings for testcases generation
max_re_generate_iterations = 10  # max iterations of generating testcases

# settings for fixing translation
max_fixing_iterations = 5

# settings for evaluation
timeout_per_task = 180  # time limit for Dafny (seconds)
max_test_threads = 5  # Note that when a task timed out, the cost will be more than expected with more threads
log_json_path = "log/MBPP/%s@%d/0.json" % (
    model,
    max_fixing_iterations,
)  # path for test log
