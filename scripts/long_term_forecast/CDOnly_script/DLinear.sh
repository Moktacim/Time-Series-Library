export CUDA_VISIBLE_DEVICES=1

model_name=DLinear

python -u run.py \
  --task_name long_term_forecast \
  --is_training 1 \
  --root_path ./dataset/Kiglis_hdf5/CD \
  --data_path training_data_5km.hdf5 \
  --model_id cdonly_30_1 \
  --model DLinear \
  --data Kiglis_Hdf5 \
  --features MS \
  --e_layers 2 \
  --d_layers 1 \
  --factor 3 \
  --enc_in 7 \
  --dec_in 7 \
  --c_out 7 \
  --batch_size 16 \
  --d_model 512 \
  --des 'Exp' \
  --itr 1 \
  --learning_rate 0.001 \
  --loss 'SMAPE'
