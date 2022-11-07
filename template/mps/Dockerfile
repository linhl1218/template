FROM openfaas/classic-watchdog:0.18.1 as watchdog

FROM nvidia/cuda:9.0-base-ubuntu16.04

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog
RUN apt-get update && apt-get install -y --no-install-recommends --allow-unauthenticated\
        cuda-samples-$CUDA_PKG_VERSION && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/local/cuda/samples/5_Simulations/nbody

RUN make -j"$(nproc)"

ENV fprocess = "./nbody -benchmark -i=10000" 
HEALTHCHECK --interval=5s CMD [ -e /tmp/.lock ] || exit 1
CMD ["fwatchdog"]
