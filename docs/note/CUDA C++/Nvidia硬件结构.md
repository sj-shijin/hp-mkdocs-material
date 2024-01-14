# Nvidia Ada架构

## 全芯片结构

- AD102 = 12 \* GPC
- GPC = 6 \* TPC
- TPC = 2 \* SM
- 1个SM：4个分区（L0指令缓存+warp调度器+分派单元+64KB寄存器+16个FP32（cuda core）+16个FP32/INT32（cuda core）+1个张量核心（tensor core）+4个加载/存储单元+4个特殊功能单元（除法，乘方，对数，三角函数））+1个（128KB L1缓存/共享内存）
- 二级缓存96MB

### RTX4090

- 128个SM
- 16384个cuda core
- 512个tensor core
- 24GB显存
- 16MB L1缓存
- 72MB L2缓存

## 第四代Tensor core



