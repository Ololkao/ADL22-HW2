export SEED=42

python multiple-choice/run_swag.py \
  --model_name_or_path "output/cs$SEED/" \
  --cache_dir "cache/cs$SEED" \
  --test_file dataset/swag_test.json \
  --max_seq_length 512 \
  --output_dir "output/test_cs$SEED" \
  --do_predict \
  --num_train_epochs 1 \
  --lr_scheduler_type linear \
  --seed $SEED \
  --fp16 \
  --report_to all \
  --resume_from_checkpoint "output/cs$SEED/"