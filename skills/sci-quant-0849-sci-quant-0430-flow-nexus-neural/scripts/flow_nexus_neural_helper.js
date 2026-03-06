/**
 * Example helper script for flow-nexus-neural configuration.
 */
function generateTrainingConfig(epochs = 100, batchSize = 32) {
  return {
    architecture: {
      type: "feedforward",
      layers: [
        { type: "dense", units: 256, activation: "relu" },
        { type: "dropout", rate: 0.3 },
        { type: "dense", units: 128, activation: "relu" },
        { type: "dense", units: 10, activation: "softmax" }
      ]
    },
    training: {
      epochs: epochs,
      batch_size: batchSize,
      learning_rate: 0.001,
      optimizer: "adam"
    }
  };
}
module.exports = { generateTrainingConfig };
