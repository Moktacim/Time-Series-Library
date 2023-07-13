if [ ! -d "./logs" ]; then
    mkdir ./logs
fi

if [ ! -d "./logs/LongForecasting" ]; then
    mkdir ./logs/LongForecasting
fi
model_name=TimesNet

python -u run.py \
  --task_name long_term_forecast \
  --is_training 1 \
  --root_path ./dataset/Kiglis_hdf5/CD \
  --data_path training_data_5km.hdf5 \
  --model_id cdonly_30_1 \
  --model $model_name \
  --data Kiglis_Hdf5 \
  --features MS \
  --seq_len 96 \
  --label_len 0 \
  --pred_len 1 \
  --e_layers 2 \
  --d_layers 1 \
  --factor 3 \
  --enc_in 7 \
  --dec_in 7 \
  --c_out 7 \
  --d_model 256 \
  --batch_size 10 \
  --d_ff 512 \
  --top_k 5 \
  --gpu 1 \
  --des 'Exp' \
  --itr 1