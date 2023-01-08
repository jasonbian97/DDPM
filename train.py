from denoising_diffusion_pytorch import Unet, GaussianDiffusion, Trainer

model = Unet(
    dim = 64,
    dim_mults = (1, 2, 4, 8)
).cuda()

diffusion = GaussianDiffusion(
    model,
    image_size = 32,
    timesteps = 1000,           # number of steps
    sampling_timesteps = 250,   # number of sampling timesteps (using ddim for faster inference [see citation for ddim paper])
    loss_type = 'l1',            # L1 or L2
    beta_schedule='cosine',
).cuda()

trainer = Trainer(
    diffusion,
    '/home/zhangxing/Projects/DiffusionModels/cifar10/train',
    train_batch_size = 64,
    train_lr = 8e-5,
    train_num_steps = 200000,         # total training steps
    gradient_accumulate_every = 2,    # gradient accumulation steps
    ema_decay = 0.995,                # exponential moving average decay
    amp = True,                        # turn on mixed precision
    save_and_sample_every=2000,       # save and sample every n steps
)

trainer.train()