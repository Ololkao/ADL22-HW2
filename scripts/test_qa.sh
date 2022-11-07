python question-answering/run_qa.py \
  --model_name_or_path "output/roberta-wwm-ext-large/qa" \
  --cache_dir "cache/roberta-wwm-ext-large" \
  --test_file format_test.json \
  --max_seq_length 512 \
  --output_dir "output/test_qa" \
  --do_predict \
  --num_train_epochs 10 \
  --lr_scheduler_type linear \
  --seed 42 \
  --fp16 \
  --report_to all \
  --resume_from_checkpoint "output/roberta-wwm-ext-large/qa"
