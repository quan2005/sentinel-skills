<template>
  <div class="bar-chart-container">
    <div class="chart-header">
      <h3 v-if="title" class="chart-title">{{ title }}</h3>
      <p v-if="subtitle" class="chart-subtitle">{{ subtitle }}</p>
    </div>

    <div class="chart-content">
      <div class="y-axis" v-if="showYAxis">
        <div
          v-for="(label, index) in yAxisLabels"
          :key="index"
          class="y-axis-label"
        >
          {{ label }}
        </div>
      </div>

      <div class="chart-bars">
        <div
          v-for="(item, index) in data"
          :key="index"
          class="bar-item"
          :style="{ height: '100%' }"
        >
          <div
            class="bar"
            :style="{
              height: `${getBarHeight(item.value)}%`,
              backgroundColor: item.color || defaultColor,
              animationDelay: `${index * 0.1}s`
            }"
            v-click
          >
            <div class="bar-value">{{ item.value }}</div>
          </div>
          <div class="bar-label">{{ item.label }}</div>
        </div>
      </div>
    </div>

    <div class="x-axis" v-if="showXAxis">
      <div
        v-for="(item, index) in data"
        :key="index"
        class="x-axis-label"
      >
        {{ item.label }}
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

interface ChartData {
  label: string
  value: number
  color?: string
}

interface Props {
  data: ChartData[]
  title?: string
  subtitle?: string
  maxValue?: number
  showYAxis?: boolean
  showXAxis?: boolean
  defaultColor?: string
  animation?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  maxValue: 100,
  showYAxis: true,
  showXAxis: true,
  defaultColor: '#3B82F6',
  animation: true
})

const maxValue = computed(() => {
  return props.maxValue || Math.max(...props.data.map(item => item.value))
})

const yAxisLabels = computed(() => {
  const max = maxValue.value
  const steps = 5
  return Array.from({ length: steps + 1 }, (_, i) => {
    return Math.round((max / steps) * (steps - i))
  })
})

const getBarHeight = (value: number) => {
  return (value / maxValue.value) * 100
}
</script>

<style scoped>
.bar-chart-container {
  width: 100%;
  height: 300px;
  display: flex;
  flex-direction: column;
  font-family: system-ui, -apple-system, sans-serif;
}

.chart-header {
  margin-bottom: 20px;
  text-align: center;
}

.chart-title {
  font-size: 18px;
  font-weight: 600;
  margin: 0 0 4px 0;
  color: #1F2937;
}

.chart-subtitle {
  font-size: 14px;
  color: #6B7280;
  margin: 0;
}

.chart-content {
  display: flex;
  flex: 1;
  align-items: flex-end;
}

.y-axis {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 40px;
  margin-right: 10px;
  font-size: 12px;
  color: #6B7280;
  text-align: right;
}

.chart-bars {
  display: flex;
  flex: 1;
  align-items: flex-end;
  justify-content: space-around;
  height: 100%;
  gap: 8px;
}

.bar-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex: 1;
  max-width: 80px;
  position: relative;
}

.bar {
  width: 100%;
  background: #3B82F6;
  border-radius: 4px 4px 0 0;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding-top: 4px;
  transition: all 0.3s ease;
  position: relative;
  animation: growBar 0.6s ease-out forwards;
}

.bar:hover {
  opacity: 0.8;
  transform: translateY(-2px);
}

.bar-value {
  color: white;
  font-size: 12px;
  font-weight: 600;
  text-shadow: 0 1px 2px rgba(0,0,0,0.2);
}

.bar-label {
  margin-top: 8px;
  font-size: 12px;
  color: #374151;
  text-align: center;
  max-width: 100%;
  word-wrap: break-word;
}

.x-axis {
  display: flex;
  justify-content: space-around;
  margin-top: 10px;
  padding-top: 5px;
  border-top: 1px solid #E5E7EB;
}

.x-axis-label {
  font-size: 12px;
  color: #6B7280;
  text-align: center;
  flex: 1;
  max-width: 80px;
}

@keyframes growBar {
  from {
    height: 0;
  }
  to {
    height: var(--final-height);
  }
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  .chart-title {
    color: #F9FAFB;
  }

  .chart-subtitle {
    color: #D1D5DB;
  }

  .bar-label {
    color: #E5E7EB;
  }

  .x-axis {
    border-top-color: #374151;
  }

  .x-axis-label,
  .y-axis-label {
    color: #9CA3AF;
  }
}
</style>