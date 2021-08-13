from package import sample_module1, sample_module2

sample_value1 = sample_module1.sample_func(18, 35)
print(sample_value1)

sample_obj = sample_module2.SampleClass(1.3, 5.8)
print(sample_obj.sample_property)
print(sample_obj.sample_method(41.5, 6.2))
