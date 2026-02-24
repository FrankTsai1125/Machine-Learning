1.using transformers==4.50.3  and colab T4 GPU
2.run method_1 for object1-4
  interpt and restart
  run method_2 for object5
  change 
  object=f"object-{6}"
  instance_prompt and generate_prompt for object6
  run method_2 for object6

3.follow below hyperparemeter:
num_inference_steps = 150
guidance_scale = 7.5
object-1
object-2
object-3
object-4

object-5
instance_prompt = "photo of a <new1> toy"        
parameter_to_train = "crossattn"       
learning_rate = 1e-5
max_train_steps = 350
train_batch_size = 3
num_inference_steps = 200 
guidance_scale = 20.0 

object-6
instance_prompt = "high quality photo of a <new1> plushie" 
generate_prompt = "high quality image of a <new1> plushie on a plate"
parameter_to_train = "crossattn_kv"            
learning_rate = 1e-5
max_train_steps = 500
train_batch_size = 3
num_inference_steps = 250 
guidance_scale = 16.0  