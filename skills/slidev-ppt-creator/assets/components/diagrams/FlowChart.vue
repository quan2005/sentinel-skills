<template>
  <div class="flow-chart-container">
    <div class="chart-header">
      <h3 v-if="title" class="chart-title">{{ title }}</h3>
      <p v-if="subtitle" class="chart-subtitle">{{ subtitle }}</p>
    </div>

    <div class="chart-content" :style="{ height: `${height}px` }">
      <svg
        :width="width"
        :height="height"
        class="flow-svg"
        :viewBox="`0 0 ${width} ${height}`"
      >
        <!-- Define arrow marker -->
        <defs>
          <marker
            id="arrowhead"
            markerWidth="10"
            markerHeight="10"
            refX="9"
            refY="3"
            orient="auto"
          >
            <polygon
              points="0 0, 10 3, 0 6"
              :fill="arrowColor"
            />
          </marker>

          <!-- Define gradient for nodes -->
          <linearGradient
            v-for="(color, index) in gradientColors"
            :key="index"
            :id="`gradient-${index}`"
            x1="0%"
            y1="0%"
            x2="100%"
            y2="100%"
          >
            <stop offset="0%" :stop-color="color.start" />
            <stop offset="100%" :stop-color="color.end" />
          </linearGradient>
        </defs>

        <!-- Render connections -->
        <g v-for="(connection, index) in connections" :key="`conn-${index}`">
          <path
            :d="connection.path"
            :stroke="connection.color || arrowColor"
            :stroke-width="connection.width || 2"
            fill="none"
            class="flow-connection"
            v-click
            :style="{ animationDelay: `${index * 0.2}s` }"
            :marker-end="connection.arrow !== false ? 'url(#arrowhead)' : ''"
          />

          <!-- Connection label -->
          <text
            v-if="connection.label"
            :x="connection.labelX"
            :y="connection.labelY"
            text-anchor="middle"
            class="connection-label"
            v-click
            :style="{ animationDelay: `${index * 0.2 + 0.1}s` }"
          >
            {{ connection.label }}
          </text>
        </g>

        <!-- Render nodes -->
        <g v-for="(node, index) in positionedNodes" :key="`node-${index}`">
          <!-- Node shape based on type -->
          <rect
            v-if="node.type === 'rectangle'"
            :x="node.x"
            :y="node.y"
            :width="node.width"
            :height="node.height"
            :rx="node.borderRadius || 8"
            :fill="node.fill || `url(#gradient-${index % gradientColors.length})`"
            :stroke="node.stroke || '#374151'"
            :stroke-width="node.strokeWidth || 2"
            class="flow-node"
            v-click
            :style="{ animationDelay: `${index * 0.15}s` }"
          />

          <ellipse
            v-else-if="node.type === 'ellipse'"
            :cx="node.x + node.width / 2"
            :cy="node.y + node.height / 2"
            :rx="node.width / 2"
            :ry="node.height / 2"
            :fill="node.fill || `url(#gradient-${index % gradientColors.length})`"
            :stroke="node.stroke || '#374151'"
            :stroke-width="node.strokeWidth || 2"
            class="flow-node"
            v-click
            :style="{ animationDelay: `${index * 0.15}s` }"
          />

          <polygon
            v-else-if="node.type === 'diamond'"
            :points="getDiamondPoints(node)"
            :fill="node.fill || `url(#gradient-${index % gradientColors.length})`"
            :stroke="node.stroke || '#374151'"
            :stroke-width="node.strokeWidth || 2"
            class="flow-node"
            v-click
            :style="{ animationDelay: `${index * 0.15}s` }"
          />

          <!-- Node text -->
          <text
            :x="node.x + node.width / 2"
            :y="node.y + node.height / 2"
            text-anchor="middle"
            dominant-baseline="middle"
            class="node-text"
            v-click
            :style="{ animationDelay: `${index * 0.15 + 0.1}s` }"
          >
            <tspan x="{{ node.x + node.width / 2 }}" dy="0">{{ node.title }}</tspan>
            <tspan
              v-if="node.subtitle"
              x="{{ node.x + node.width / 2 }}"
              dy="16"
              class="node-subtitle"
            >
              {{ node.subtitle }}
            </tspan>
          </text>
        </g>
      </svg>
    </div>

    <!-- Legend -->
    <div v-if="showLegend" class="chart-legend">
      <div class="legend-title">Legend</div>
      <div class="legend-items">
        <div
          v-for="(item, index) in legendItems"
          :key="index"
          class="legend-item"
        >
          <div
            class="legend-shape"
            :style="getLegendShapeStyle(item.type)"
          />
          <span class="legend-text">{{ item.label }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

interface FlowNode {
  id: string
  title: string
  subtitle?: string
  type?: 'rectangle' | 'ellipse' | 'diamond'
  width?: number
  height?: number
  fill?: string
  stroke?: string
  strokeWidth?: number
  borderRadius?: number
  position?: { x: number; y: number }
}

interface FlowConnection {
  from: string
  to: string
  label?: string
  color?: string
  width?: number
  arrow?: boolean
}

interface LayoutConfig {
  type: 'vertical' | 'horizontal' | 'grid' | 'custom'
  spacing?: { x: number; y: number }
  columns?: number
}

interface Props {
  nodes: FlowNode[]
  connections: FlowConnection[]
  title?: string
  subtitle?: string
  width?: number
  height?: number
  layout?: LayoutConfig
  showLegend?: boolean
  arrowColor?: string
  nodeColors?: string[]
}

const props = withDefaults(defineProps<Props>(), {
  width: 800,
  height: 400,
  layout: () => ({ type: 'vertical', spacing: { x: 120, y: 100 } }),
  showLegend: false,
  arrowColor: '#6B7280',
  nodeColors: () => ['#3B82F6', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6', '#EC4899']
})

const gradientColors = computed(() => [
  { start: '#3B82F6', end: '#2563EB' },
  { start: '#10B981', end: '#059669' },
  { start: '#F59E0B', end: '#D97706' },
  { start: '#EF4444', end: '#DC2626' },
  { start: '#8B5CF6', end: '#7C3AED' },
  { start: '#EC4899', end: '#DB2777' }
])

const positionedNodes = computed(() => {
  return props.nodes.map((node, index) => {
    const defaultWidth = 120
    const defaultHeight = 60

    if (node.position && props.layout.type === 'custom') {
      return {
        ...node,
        x: node.position.x,
        y: node.position.y,
        width: node.width || defaultWidth,
        height: node.height || defaultHeight
      }
    }

    const { x, y } = calculateNodePosition(index, node.width || defaultWidth, node.height || defaultHeight)

    return {
      ...node,
      x,
      y,
      width: node.width || defaultWidth,
      height: node.height || defaultHeight
    }
  })
})

const calculatedConnections = computed(() => {
  return props.connections.map(conn => {
    const fromNode = positionedNodes.value.find(n => n.id === conn.from)
    const toNode = positionedNodes.value.find(n => n.id === conn.to)

    if (!fromNode || !toNode) return null

    const fromX = fromNode.x + fromNode.width / 2
    const fromY = fromNode.y + fromNode.height / 2
    const toX = toNode.x + toNode.width / 2
    const toY = toNode.y + toNode.height / 2

    const path = createCurvedPath(fromX, fromY, toX, toY)

    return {
      ...conn,
      path,
      labelX: (fromX + toX) / 2,
      labelY: (fromY + toY) / 2 - 10
    }
  }).filter(Boolean) as any[]
})

const legendItems = computed(() => {
  const uniqueTypes = [...new Set(props.nodes.map(n => n.type || 'rectangle'))]
  return uniqueTypes.map(type => ({
    type,
    label: type.charAt(0).toUpperCase() + type.slice(1)
  }))
})

const calculateNodePosition = (index: number, width: number, height: number) => {
  const spacing = props.layout.spacing || { x: 120, y: 100 }

  switch (props.layout.type) {
    case 'vertical':
      return {
        x: props.width / 2 - width / 2,
        y: 50 + index * spacing.y
      }

    case 'horizontal':
      return {
        x: 50 + index * spacing.x,
        y: props.height / 2 - height / 2
      }

    case 'grid':
      const cols = props.layout.columns || 3
      const row = Math.floor(index / cols)
      const col = index % cols
      return {
        x: 100 + col * spacing.x,
        y: 50 + row * spacing.y
      }

    default:
      return { x: 50, y: 50 }
  }
}

const createCurvedPath = (x1: number, y1: number, x2: number, y2: number) => {
  const dx = x2 - x1
  const dy = y2 - y1
  const dr = Math.sqrt(dx * dx + dy * dy)

  const offsetX = dx * 0.2
  const offsetY = dy * 0.2

  return `M ${x1} ${y1} Q ${x1 + offsetX} ${y1 + offsetY}, ${x2} ${y2}`
}

const getDiamondPoints = (node: any) => {
  const cx = node.x + node.width / 2
  const cy = node.y + node.height / 2
  const w = node.width / 2
  const h = node.height / 2

  return `${cx},${cy - h} ${cx + w},${cy} ${cx},${cy + h} ${cx - w},${cy}`
}

const getLegendShapeStyle = (type: string) => {
  const baseStyle = {
    width: '20px',
    height: '14px',
    backgroundColor: '#3B82F6',
    border: '2px solid #374151'
  }

  switch (type) {
    case 'ellipse':
      return { ...baseStyle, borderRadius: '50%' }
    case 'diamond':
      return { ...baseStyle, transform: 'rotate(45deg)' }
    default:
      return { ...baseStyle, borderRadius: '2px' }
  }
}
</script>

<style scoped>
.flow-chart-container {
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
  justify-content: center;
  align-items: center;
  background: #FAFAFA;
  border-radius: 8px;
  border: 1px solid #E5E7EB;
  overflow: hidden;
}

.flow-svg {
  max-width: 100%;
  height: auto;
}

.flow-node {
  cursor: pointer;
  transition: all 0.3s ease;
  animation: fadeIn 0.6s ease-out forwards;
}

.flow-node:hover {
  filter: brightness(1.1);
  transform: scale(1.02);
}

.flow-connection {
  animation: drawLine 0.8s ease-out forwards;
}

.connection-label {
  font-size: 12px;
  fill: #6B7280;
  font-weight: 500;
  animation: fadeIn 0.6s ease-out forwards;
}

.node-text {
  font-size: 14px;
  font-weight: 600;
  fill: #1F2937;
  pointer-events: none;
  animation: fadeIn 0.6s ease-out forwards;
}

.node-subtitle {
  font-size: 11px;
  font-weight: 400;
  fill: #6B7280;
}

.chart-legend {
  margin-top: 16px;
  display: flex;
  align-items: center;
  gap: 16px;
  font-size: 12px;
}

.legend-title {
  font-weight: 600;
  color: #374151;
}

.legend-items {
  display: flex;
  gap: 12px;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 6px;
}

.legend-shape {
  border: 2px solid #374151;
}

.legend-text {
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

@keyframes drawLine {
  from {
    stroke-dasharray: 1000;
    stroke-dashoffset: 1000;
  }
  to {
    stroke-dashoffset: 0;
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

  .chart-content {
    background: #1F2937;
    border-color: #374151;
  }

  .connection-label {
    fill: #9CA3AF;
  }

  .node-text {
    fill: #F9FAFB;
  }

  .node-subtitle {
    fill: #D1D5DB;
  }

  .legend-title {
    color: #F9FAFB;
  }

  .legend-text {
    color: #9CA3AF;
  }
}

/* Responsive design */
@media (max-width: 768px) {
  .chart-legend {
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
  }

  .legend-items {
    flex-wrap: wrap;
  }
}
</style>