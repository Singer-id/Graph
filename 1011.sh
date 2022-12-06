#python T5.py --except_domain taxi --n_epochs 1 --train_batch_size 4 --seed 555 --auxiliary_task_ratio 0.0  --base
#python T5.py --model_checkpoint save/t5-smallt5_except_domain_taxi_lr_0.0001_epoch_1_seed_555_batch_size_4_auxiliary_task_0.0_base_True_task2first_False/ --n_epochs 5 --train_batch_size 4 --seed 555 --auxiliary_task_ratio 0.0 --fewshot 0.01 --mode finetune --base
#python T5.py --model_checkpoint save/t5-smallt5_except_domain_taxi_lr_0.0001_epoch_1_seed_555_batch_size_4_auxiliary_task_0.0_base_True_task2first_False/ --n_epochs 5 --train_batch_size 4 --seed 555 --auxiliary_task_ratio 0.0 --fewshot 0.05 --mode finetune --base
#python T5.py --model_checkpoint save/t5-smallt5_except_domain_taxi_lr_0.0001_epoch_1_seed_555_batch_size_4_auxiliary_task_0.0_base_True_task2first_False/ --n_epochs 5 --train_batch_size 4 --seed 555 --auxiliary_task_ratio 0.0 --fewshot 0.1 --mode finetune --base

python T5.py --except_domain taxi --n_epochs 1 --train_batch_size 4 --seed 555 --auxiliary_task_ratio 1.0  --task2first
python T5.py --model_checkpoint save/t5-smallt5_except_domain_taxi_lr_0.0001_epoch_1_seed_555_batch_size_4_auxiliary_task_1.0_base_False_task2first_True/ --n_epochs 5 --train_batch_size 4 --seed 555 --auxiliary_task_ratio 1.0 --fewshot 0.01 --mode finetune --task2first
python T5.py --model_checkpoint save/t5-smallt5_except_domain_taxi_lr_0.0001_epoch_1_seed_555_batch_size_4_auxiliary_task_1.0_base_False_task2first_True/ --n_epochs 5 --train_batch_size 4 --seed 555 --auxiliary_task_ratio 1.0 --fewshot 0.05 --mode finetune --task2first
python T5.py --model_checkpoint save/t5-smallt5_except_domain_taxi_lr_0.0001_epoch_1_seed_555_batch_size_4_auxiliary_task_1.0_base_False_task2first_True/ --n_epochs 5 --train_batch_size 4 --seed 555 --auxiliary_task_ratio 1.0 --fewshot 0.1 --mode finetune --task2first

python T5.py --except_domain taxi --n_epochs 1 --train_batch_size 4 --seed 555 --auxiliary_task_ratio 0.25  --task2first
python T5.py --model_checkpoint save/t5-smallt5_except_domain_taxi_lr_0.0001_epoch_1_seed_555_batch_size_4_auxiliary_task_0.25_base_False_task2first_True/ --n_epochs 5 --train_batch_size 4 --seed 555 --auxiliary_task_ratio 0.25 --fewshot 0.01 --mode finetune --task2first
python T5.py --model_checkpoint save/t5-smallt5_except_domain_taxi_lr_0.0001_epoch_1_seed_555_batch_size_4_auxiliary_task_0.25_base_False_task2first_True/ --n_epochs 5 --train_batch_size 4 --seed 555 --auxiliary_task_ratio 0.25 --fewshot 0.05 --mode finetune --task2first
python T5.py --model_checkpoint save/t5-smallt5_except_domain_taxi_lr_0.0001_epoch_1_seed_555_batch_size_4_auxiliary_task_0.25_base_False_task2first_True/ --n_epochs 5 --train_batch_size 4 --seed 555 --auxiliary_task_ratio 0.25 --fewshot 0.1 --mode finetune --task2first

python T5.py --except_domain taxi --n_epochs 1 --train_batch_size 4 --seed 555 --auxiliary_task_ratio 0.5  --task2first
python T5.py --model_checkpoint save/t5-smallt5_except_domain_taxi_lr_0.0001_epoch_1_seed_555_batch_size_4_auxiliary_task_0.5_base_False_task2first_True/ --n_epochs 5 --train_batch_size 4 --seed 555 --auxiliary_task_ratio 0.5 --fewshot 0.01 --mode finetune --task2first
python T5.py --model_checkpoint save/t5-smallt5_except_domain_taxi_lr_0.0001_epoch_1_seed_555_batch_size_4_auxiliary_task_0.5_base_False_task2first_True/ --n_epochs 5 --train_batch_size 4 --seed 555 --auxiliary_task_ratio 0.5 --fewshot 0.05 --mode finetune --task2first
python T5.py --model_checkpoint save/t5-smallt5_except_domain_taxi_lr_0.0001_epoch_1_seed_555_batch_size_4_auxiliary_task_0.5_base_False_task2first_True/ --n_epochs 5 --train_batch_size 4 --seed 555 --auxiliary_task_ratio 0.5 --fewshot 0.1 --mode finetune --task2first

python T5.py --except_domain taxi --n_epochs 1 --train_batch_size 4 --seed 555 --auxiliary_task_ratio 0.75  --task2first
python T5.py --model_checkpoint save/t5-smallt5_except_domain_taxi_lr_0.0001_epoch_1_seed_555_batch_size_4_auxiliary_task_0.75_base_False_task2first_True/ --n_epochs 5 --train_batch_size 4 --seed 555 --auxiliary_task_ratio 0.75 --fewshot 0.01 --mode finetune --task2first
python T5.py --model_checkpoint save/t5-smallt5_except_domain_taxi_lr_0.0001_epoch_1_seed_555_batch_size_4_auxiliary_task_0.75_base_False_task2first_True/ --n_epochs 5 --train_batch_size 4 --seed 555 --auxiliary_task_ratio 0.75 --fewshot 0.05 --mode finetune --task2first
python T5.py --model_checkpoint save/t5-smallt5_except_domain_taxi_lr_0.0001_epoch_1_seed_555_batch_size_4_auxiliary_task_0.75_base_False_task2first_True/ --n_epochs 5 --train_batch_size 4 --seed 555 --auxiliary_task_ratio 0.75 --fewshot 0.1 --mode finetune --task2first

