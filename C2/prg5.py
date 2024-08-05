print("SJC23MCA-2001 : ABHIRAMI VINOD")
print("Batch : MCA 2023-25")
import numpy as np
even_numbers=np.arange(2,31,2)
slice_result=even_numbers[2:9:2]
last_3_elements=even_numbers[-3:]
alternate_elements=even_numbers[::2]
last_3_alternate_elements=alternate_elements[-3:]
print("Original Array: ",even_numbers)
print("Elements from 2 to 8 with step 2: ",slice_result)
print("Last 3 element sof the array using negative index",last_3_elements)
print("Alternate elements of the array: ",alternate_elements)
print("Last 3 Alternate elements: ",last_3_alternate_elements)