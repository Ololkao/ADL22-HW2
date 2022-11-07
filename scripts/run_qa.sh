export SEED=42

python question-answering/run_qa.py \
  --model_name_or_path hfl/chinese-roberta-wwm-ext-large \
  --cache_dir "cache/qa$SEED" \
  --train_file dataset/squad_train.json \
  --validation_file dataset/squad_valid.json \
  --max_seq_length 512 \
  --doc_stride 128 \
  --n_best_size 20 \
  --max_answer_length 30 \
  --output_dir "output/qa$SEED" \
  --overwrite_output_dir \
  --do_train \
  --do_eval \
  --evaluation_strategy epoch \
  --per_device_train_batch_size 8 \
  --per_device_eval_batch_size 8 \
  --gradient_accumulation_steps 1 \
  --learning_rate 3e-5 \
  --weight_decay 1e-4 \
  --num_train_epochs 3 \
  --lr_scheduler_type linear \
  --warmup_ratio 0.0 \
  --save_strategy steps \
  --save_steps 500 \
  --seed $SEED \
  --fp16 \
  --report_to all