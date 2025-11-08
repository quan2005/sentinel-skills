<template>
  <div class="quiz-container">
    <div class="quiz-header">
      <h3 v-if="title" class="quiz-title">{{ title }}</h3>
      <p v-if="subtitle" class="quiz-subtitle">{{ subtitle }}</p>
    </div>

    <div v-if="!quizComplete" class="quiz-content">
      <!-- Progress indicator -->
      <div class="quiz-progress">
        <div class="progress-text">
          Question {{ currentQuestionIndex + 1 }} of {{ questions.length }}
        </div>
        <div class="progress-bar">
          <div
            class="progress-fill"
            :style="{ width: `${progressPercentage}%` }"
          />
        </div>
      </div>

      <!-- Current question -->
      <div class="question-card" v-click>
        <div class="question-text">
          {{ currentQuestion.text }}
        </div>

        <div v-if="currentQuestion.hint" class="question-hint">
          <span class="hint-icon">💡</span>
          {{ currentQuestion.hint }}
        </div>
      </div>

      <!-- Answer options -->
      <div class="answer-options">
        <div
          v-for="(option, index) in currentQuestion.options"
          :key="index"
          class="answer-option"
          :class="{
            'selected': selectedAnswer === index,
            'correct': showResult && isCorrectAnswer(index),
            'incorrect': showResult && selectedAnswer === index && !isCorrectAnswer(index)
          }"
          @click="selectAnswer(index)"
          v-click
          :style="{ animationDelay: `${index * 0.1}s` }"
        >
          <div class="option-indicator">
            <span class="option-letter">{{ String.fromCharCode(65 + index) }}</span>
            <div class="option-icon">
              <CheckIcon v-if="showResult && isCorrectAnswer(index)" />
              <XIcon v-else-if="showResult && selectedAnswer === index && !isCorrectAnswer(index)" />
              <div v-else-if="selectedAnswer === index" class="selected-dot" />
            </div>
          </div>
          <div class="option-text">{{ option }}</div>
        </div>
      </div>

      <!-- Action buttons -->
      <div class="quiz-actions">
        <button
          v-if="!showResult && selectedAnswer !== null"
          @click="submitAnswer"
          class="submit-button"
          v-click
        >
          Submit Answer
        </button>

        <button
          v-if="showResult"
          @click="nextQuestion"
          class="next-button"
          v-click
        >
          {{ isLastQuestion ? 'See Results' : 'Next Question' }}
        </button>
      </div>

      <!-- Feedback -->
      <div v-if="showResult && currentQuestion.explanation" class="answer-feedback">
        <div
          class="feedback-content"
          :class="{
            'correct-feedback': isCorrectAnswer(selectedAnswer),
            'incorrect-feedback': !isCorrectAnswer(selectedAnswer)
          }"
        >
          <div class="feedback-icon">
            <CheckIcon v-if="isCorrectAnswer(selectedAnswer)" />
            <XIcon v-else />
          </div>
          <div class="feedback-text">
            <div class="feedback-title">
              {{ isCorrectAnswer(selectedAnswer) ? 'Correct!' : 'Not quite' }}
            </div>
            <div class="feedback-explanation">
              {{ currentQuestion.explanation }}
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Quiz results -->
    <div v-else class="quiz-results">
      <div class="results-header">
        <div class="results-icon">
          <TrophyIcon v-if="scorePercentage >= 80" />
          <MedalIcon v-else-if="scorePercentage >= 60" />
          <BookIcon v-else />
        </div>
        <h3 class="results-title">Quiz Complete!</h3>
        <div class="results-score">
          {{ correctAnswers }} out of {{ questions.length }} correct
        </div>
        <div class="results-percentage">{{ scorePercentage }}%</div>
      </div>

      <div class="results-message">
        {{ getResultMessage() }}
      </div>

      <div class="results-details">
        <div class="detail-item">
          <span class="detail-label">Correct Answers:</span>
          <span class="detail-value correct">{{ correctAnswers }}</span>
        </div>
        <div class="detail-item">
          <span class="detail-label">Incorrect Answers:</span>
          <span class="detail-value incorrect">{{ questions.length - correctAnswers }}</span>
        </div>
        <div class="detail-item">
          <span class="detail-label">Time Taken:</span>
          <span class="detail-value">{{ formatTime(timeTaken) }}</span>
        </div>
      </div>

      <button
        @click="restartQuiz"
        class="restart-button"
        v-click
      >
        Try Again
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'

interface Question {
  text: string
  options: string[]
  correctAnswer: number
  explanation?: string
  hint?: string
}

interface Props {
  questions: Question[]
  title?: string
  subtitle?: string
  showProgress?: boolean
  allowRetry?: boolean
  timeLimit?: number // in seconds
}

const props = withDefaults(defineProps<Props>(), {
  showProgress: true,
  allowRetry: true
})

const currentQuestionIndex = ref(0)
const selectedAnswer = ref<number | null>(null)
const showResult = ref(false)
const quizComplete = ref(false)
const correctAnswers = ref(0)
const startTime = ref(Date.now())
const timeTaken = ref(0)

const currentQuestion = computed(() => {
  return props.questions[currentQuestionIndex.value]
})

const progressPercentage = computed(() => {
  return ((currentQuestionIndex.value + 1) / props.questions.length) * 100
})

const scorePercentage = computed(() => {
  return Math.round((correctAnswers.value / props.questions.length) * 100)
})

const isLastQuestion = computed(() => {
  return currentQuestionIndex.value === props.questions.length - 1
})

const isCorrectAnswer = (index: number) => {
  return index === currentQuestion.value.correctAnswer
}

const selectAnswer = (index: number) => {
  if (!showResult.value) {
    selectedAnswer.value = index
  }
}

const submitAnswer = () => {
  if (selectedAnswer.value !== null) {
    showResult.value = true

    if (isCorrectAnswer(selectedAnswer.value)) {
      correctAnswers.value++
    }
  }
}

const nextQuestion = () => {
  if (isLastQuestion.value) {
    completeQuiz()
  } else {
    currentQuestionIndex.value++
    selectedAnswer.value = null
    showResult.value = false
  }
}

const completeQuiz = () => {
  timeTaken.value = Math.floor((Date.now() - startTime.value) / 1000)
  quizComplete.value = true
}

const restartQuiz = () => {
  currentQuestionIndex.value = 0
  selectedAnswer.value = null
  showResult.value = false
  quizComplete.value = false
  correctAnswers.value = 0
  startTime.value = Date.now()
  timeTaken.value = 0
}

const getResultMessage = () => {
  const percentage = scorePercentage.value
  if (percentage >= 90) return "Outstanding! You've mastered this topic!"
  if (percentage >= 80) return "Excellent work! You have a strong understanding."
  if (percentage >= 70) return "Good job! You understand most of the material."
  if (percentage >= 60) return "Not bad! A bit more practice would help."
  return "Keep studying! Review the material and try again."
}

const formatTime = (seconds: number) => {
  const mins = Math.floor(seconds / 60)
  const secs = seconds % 60
  return `${mins}:${secs.toString().padStart(2, '0')}`
}

// Icon components
const CheckIcon = () => '✓'
const XIcon = () => '✗'
const TrophyIcon = () => '🏆'
const MedalIcon = () => '🥇'
const BookIcon = () => '📚'

onMounted(() => {
  startTime.value = Date.now()
})
</script>

<style scoped>
.quiz-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 24px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  font-family: system-ui, -apple-system, sans-serif;
}

.quiz-header {
  text-align: center;
  margin-bottom: 24px;
}

.quiz-title {
  font-size: 24px;
  font-weight: 700;
  color: #1F2937;
  margin: 0 0 8px 0;
}

.quiz-subtitle {
  font-size: 16px;
  color: #6B7280;
  margin: 0;
}

.quiz-progress {
  margin-bottom: 24px;
}

.progress-text {
  font-size: 14px;
  color: #6B7280;
  margin-bottom: 8px;
  text-align: center;
}

.progress-bar {
  width: 100%;
  height: 8px;
  background: #E5E7EB;
  border-radius: 4px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #3B82F6, #1D4ED8);
  transition: width 0.3s ease;
}

.question-card {
  background: #F9FAFB;
  border: 2px solid #E5E7EB;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 24px;
  animation: fadeIn 0.5s ease-out;
}

.question-text {
  font-size: 18px;
  font-weight: 600;
  color: #1F2937;
  line-height: 1.4;
}

.question-hint {
  margin-top: 12px;
  padding: 8px 12px;
  background: #FEF3C7;
  border-left: 4px solid #F59E0B;
  border-radius: 4px;
  font-size: 14px;
  color: #92400E;
  display: flex;
  align-items: center;
  gap: 8px;
}

.hint-icon {
  font-size: 16px;
}

.answer-options {
  margin-bottom: 24px;
}

.answer-option {
  display: flex;
  align-items: center;
  padding: 16px;
  margin-bottom: 12px;
  border: 2px solid #E5E7EB;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
  background: white;
  animation: slideIn 0.5s ease-out forwards;
}

.answer-option:hover:not(.selected):not(.correct):not(.incorrect) {
  border-color: #3B82F6;
  background: #F0F9FF;
}

.answer-option.selected {
  border-color: #3B82F6;
  background: #EFF6FF;
}

.answer-option.correct {
  border-color: #10B981;
  background: #F0FDF4;
}

.answer-option.incorrect {
  border-color: #EF4444;
  background: #FEF2F2;
}

.option-indicator {
  width: 40px;
  height: 40px;
  margin-right: 16px;
  position: relative;
}

.option-letter {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-weight: 600;
  color: #6B7280;
  font-size: 14px;
}

.selected .option-letter {
  color: #3B82F6;
}

.correct .option-letter,
.incorrect .option-letter {
  display: none;
}

.option-icon {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 20px;
}

.selected-dot {
  width: 8px;
  height: 8px;
  background: #3B82F6;
  border-radius: 50%;
}

.option-text {
  flex: 1;
  font-size: 16px;
  color: #374151;
  line-height: 1.4;
}

.quiz-actions {
  text-align: center;
  margin-bottom: 20px;
}

.submit-button,
.next-button,
.restart-button {
  background: #3B82F6;
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.submit-button:hover,
.next-button:hover,
.restart-button:hover {
  background: #2563EB;
}

.answer-feedback {
  margin-bottom: 20px;
}

.feedback-content {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 16px;
  border-radius: 8px;
  animation: fadeIn 0.5s ease-out;
}

.correct-feedback {
  background: #F0FDF4;
  border-left: 4px solid #10B981;
}

.incorrect-feedback {
  background: #FEF2F2;
  border-left: 4px solid #EF4444;
}

.feedback-icon {
  font-size: 24px;
}

.feedback-title {
  font-weight: 600;
  margin-bottom: 4px;
  color: #1F2937;
}

.feedback-explanation {
  font-size: 14px;
  color: #6B7280;
  line-height: 1.4;
}

.quiz-results {
  text-align: center;
  animation: fadeIn 0.5s ease-out;
}

.results-header {
  margin-bottom: 24px;
}

.results-icon {
  font-size: 48px;
  margin-bottom: 16px;
}

.results-title {
  font-size: 28px;
  font-weight: 700;
  color: #1F2937;
  margin: 0 0 8px 0;
}

.results-score {
  font-size: 18px;
  color: #6B7280;
  margin-bottom: 4px;
}

.results-percentage {
  font-size: 36px;
  font-weight: 700;
  color: #3B82F6;
}

.results-message {
  font-size: 18px;
  color: #374151;
  margin-bottom: 24px;
  line-height: 1.4;
}

.results-details {
  display: flex;
  justify-content: center;
  gap: 24px;
  margin-bottom: 24px;
  padding: 16px;
  background: #F9FAFB;
  border-radius: 8px;
}

.detail-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.detail-label {
  font-size: 12px;
  color: #6B7280;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.detail-value {
  font-size: 20px;
  font-weight: 600;
  color: #1F2937;
}

.detail-value.correct {
  color: #10B981;
}

.detail-value.incorrect {
  color: #EF4444;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(-20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  .quiz-container {
    background: #1F2937;
    color: #F9FAFB;
  }

  .quiz-title {
    color: #F9FAFB;
  }

  .question-card {
    background: #374151;
    border-color: #4B5563;
  }

  .question-text {
    color: #F9FAFB;
  }

  .answer-option {
    background: #374151;
    border-color: #4B5563;
  }

  .option-text {
    color: #E5E7EB;
  }

  .results-details {
    background: #374151;
  }
}

/* Responsive design */
@media (max-width: 640px) {
  .quiz-container {
    padding: 16px;
  }

  .answer-option {
    padding: 12px;
  }

  .option-indicator {
    width: 32px;
    height: 32px;
    margin-right: 12px;
  }

  .results-details {
    flex-direction: column;
    gap: 16px;
  }
}
</style>