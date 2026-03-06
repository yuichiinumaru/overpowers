# During compilation - note the device and shapes
model = MyModel().eval()           # What device? CPU or .cuda()?
inp = torch.randn(2, 10)           # What device? What shape?
compiled_so = torch._inductor.aot_compile(model, (inp,))

# During loading - device type MUST match compilation
loaded = torch._export.aot_load(compiled_so, "???")  # Must match model/input device above

# During inference - device and shapes MUST match
out = loaded(inp.to("???"))  # Must match compile device, shape must match

torch._export.aot_compile()  # Deprecated
torch._export.aot_load()     # Deprecated

torch._inductor.aoti_compile_and_package()
torch._inductor.aoti_load_package()
