import onnxruntime as ort

providers = [
    (
        'OpenVINOExecutionProvider',
        {
            'device_type': 'MYRIAD_FP16',
            'enable_vpu_fast_compile': False,
            'num_of_threads': 1,
            'use_compiled_network': False,
        },
    )
]

ort_sess = ort.InferenceSession('model.onnx', providers=providers)
in_names = [inp.name for inp in ort_sess.get_inputs()]
out_name = [output.name for output in ort_sess.get_outputs()]

some_data_output = ort_sess.run(out_name, {in_names[0]: some_data_input})