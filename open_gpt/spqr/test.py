from quantize import *

quantized_path = "./quantized"
before_args, quantized_args = quant("openlm-research/open_llama_3b", quantized_path)

