export SEED=42

python question-answering/run_qa.py \
  --model_name_or_path "output/qa$SEED/" \
  --test_file format_test.json \
  --max_seq_length 512 \
  --output_dir "output/test_qa$SEED" \
  --do_predict \
  --num_train_epochs 1 \
  --lr_scheduler_type linear \
  --seed $SEED \
  --fp16 \
  --report_to all \
  --resume_from_checkpoint "output/qa$SEED/"