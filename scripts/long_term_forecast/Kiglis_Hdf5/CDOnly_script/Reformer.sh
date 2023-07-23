if [ ! -d "./logs" ]; then
    mkdir ./logs
fi

if [ ! -d "./logs/LongForecasting" ]; then
    mkdir ./logs/LongForecasting
fi

model_name=Reformer

python -u run.py \
  --task_name long_term_forecast \
  --is_training 1 \
  --root_path ./dataset/Kiglis_hdf5/CD \
  --data_path training_data_9km.hdf5 \
  --model_id cdonly_30_1 \
  --model Reformer \
  --data Kiglis_Hdf5 \
  --features MS \
  --seq_len 96 \
  --label_len 0 \
  --pred_len 1 \
  --e_layers 2 \
  --d_layers 1 \
  --factor 3 \
  --enc_in 30 \
  --dec_in 30 \
  --c_out 30 \
  --batch_size 10 \
  --d_model 512 \
  --des 'Exp' \
  --train_epochs 3 \
  --itr 1 \
  #--learning_rate 0.001 \
  # --train_epochs 10 \
  # --patience 10