<template>
  <div class="pie-chart-container">
    <div class="chart-header">
      <h3 v-if="title" class="chart-title">{{ title }}</h3>
      <p v-if="subtitle" class="chart-subtitle">{{ subtitle }}</p>
    </div>

    <div class="chart-content">
      <div class="pie-chart">
        <svg
          :width="size"
          :height="size"
          viewBox="0 0 100 100"
          class="pie-svg"
        >
          <!-- Background circle -->
          <circle
            cx="50"
            cy="50"
            r="40"
            fill="none"
            stroke="#E5E7EB"
            stroke-width="2"
          />

          <!-- Pie slices -->
          <g v-for="(slice, index) in slices" :key="index">
            <path
              :d="slice.path"
              :fill="slice.color"
              :stroke="strokeColor"
              :stroke-width="strokeWidth"
              class="pie-slice"
              v-click
              :style="{ animationDelay: `${index * 0.1}s` }"
            />
          </g>

          <!-- Center circle for donut chart -->
          <circle
            v-if="donut"
            cx="50"
            cy="50"
            r="centerRadius"
            fill="white"
          />

          <!-- Center text -->
          <text
            v-if="centerText"
            x="50"
            y="50"
            text-anchor="middle"
            dominant-baseline="middle"
            class="center-text"
            :style="{ fontSize: centerFontSize }"
          >
            {{ centerText }}
          </text>
        </svg>
      </div>

      <!-- Legend -->
      <div v-if="showLegend" class="chart-legend">
        <div
          v-for="(item, index) in legendData"
          :key="index"
          class="legend-item"
          v-click
          :style="{ animationDelay: `${index * 0.1}s` }"
        >
          <div
            class="legend-color"
            :style="{ backgroundColor: item.color }"
          />
          <div class="legend-text">
            <div class="legend-label">{{ item.label }}</div>
            <div class="legend-value">{{ item.value }} ({{ item.percentage }}%)</div>
          </div>
        </div>
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
  size?: number
  donut?: boolean
  centerRadius?: number
  centerText?: string
  centerFontSize?: string
  showLegend?: boolean
  strokeColor?: string
  strokeWidth?: number
  colors?: string[]
}

const props = withDefaults(defineProps<Props>(), {
  size: 200,
  donut: false,
  centerRadius: 20,
  centerFontSize: '12px',
  showLegend: true,
  strokeColor: '#FFFFFF',
  strokeWidth: 2,
  colors: () => [
    '#3B82F6', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6',
    '#EC4899', '#14B8A6', '#F97316', '#06B6D4', '#84CC16'
  ]
})

const total = computed(() => {
  return props.data.reduce((sum, item) => sum + item.value, 0)
})

const legendData = computed(() => {
  return props.data.map((item, index) => ({
    ...item,
    color: item.color || props.colors[index % props.colors.length],
    percentage: ((item.value / total.value) * 100).toFixed(1)
  }))
})

const slices = computed(() => {
  let currentAngle = -90 // Start from top

  return legendData.value.map((item) => {
    const percentage = item.value / total.value
    const angle = percentage * 360

    const path = createPieSlice(currentAngle, currentAngle + angle, 40)
    currentAngle += angle

    return {
      path,
      color: item.color,
      value: item.value,
      label: item.label
    }
  })
})

const createPieSlice = (startAngle: number, endAngle: number, radius: number) => {
  const startAngleRad = (startAngle * Math.PI) / 180
  const endAngleRad = (endAngle * Math.PI) / 180

  const x1 = 50 + radius * Math.cos(startAngleRad)
  const y1 = 50 + radius * Math.sin(startAngleRad)
  const x2 = 50 + radius * Math.cos(endAngleRad)
  const y2 = 50 + radius * Math.sin(endAngleRad)

  const largeArcFlag = endAngle - startAngle > 180 ? 1 : 0

  return `M 50 50 L ${x1} ${y1} A ${radius} ${radius} 0 ${largeArcFlag} 1 ${x2} ${y2} Z`
}
</script>

<style scoped>
.pie-chart-container {
  width: 100%;
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
  align-items: center;
  gap: 30px;
  flex-wrap: wrap;
  justify-content: center;
}

.pie-chart {
  display: flex;
  justify-content: center;
}

.pie-svg {
  filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.1));
}

.pie-slice {
  cursor: pointer;
  transition: all 0.3s ease;
  animation: fadeIn 0.6s ease-out forwards;
  transform-origin: 50% 50%;
}

.pie-slice:hover {
  transform: scale(1.05);
  filter: brightness(1.1);
}

.center-text {
  fill: #1F2937;
  font-weight: 600;
  font-family: system-ui, -apple-system, sans-serif;
}

.chart-legend {
  display: flex;
  flex-direction: column;
  gap: 8px;
  max-width: 200px;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 4px 8px;
  border-radius: 6px;
  transition: background-color 0.2s ease;
  animation: slideIn 0.6s ease-out forwards;
}

.legend-item:hover {
  background-color: #F3F4F6;
}

.legend-color {
  width: 16px;
  height: 16px;
  border-radius: 4px;
  border: 2px solid #FFFFFF;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.legend-text {
  flex: 1;
}

.legend-label {
  font-size: 14px;
  font-weight: 500;
  color: #1F2937;
  line-height: 1.2;
}

.legend-value {
  font-size: 12px;
  color: #6B7280;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: scale(0.8);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(-10px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
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

  .legend-item:hover {
    background-color: #374151;
  }

  .legend-label {
    color: #F9FAFB;
  }

  .legend-value {
    color: #9CA3AF;
  }

  .center-text {
    fill: #F9FAFB;
  }
}

/* Responsive design */
@media (max-width: 768px) {
  .chart-content {
    flex-direction: column;
    gap: 20px;
  }

  .chart-legend {
    max-width: 100%;
    width: 100%;
  }
}
</style>