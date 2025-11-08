#!/usr/bin/env python3
"""
Content Analyzer for Slidev PPT Creator
Analyzes user input to determine presentation type, structure, and requirements.
"""

import re
import json
from typing import Dict, List, Tuple, Any

class ContentAnalyzer:
    def __init__(self):
        # Keywords for different presentation types
        self.type_keywords = {
            'business': [
                'business', 'company', 'product', 'market', 'sales', 'marketing',
                'revenue', 'profit', 'investment', 'strategy', 'proposal', 'pitch',
                '商业', '企业', '产品', '市场', '销售', '营销', '收入', '利润', '投资', '战略', '提案'
            ],
            'technical': [
                'technical', 'technology', 'code', 'programming', 'development',
                'architecture', 'system', 'software', 'api', 'database', 'algorithm',
                '技术', '代码', '编程', '开发', '架构', '系统', '软件', '算法', '数据库'
            ],
            'education': [
                'education', 'training', 'teaching', 'learning', 'course', 'tutorial',
                'lesson', 'study', 'academic', 'knowledge', 'skill', 'workshop',
                '教育', '培训', '教学', '学习', '课程', '教程', '知识', '技能', '工作坊'
            ]
        }

        # Keywords for visual elements
        self.visual_keywords = {
            'chart': ['chart', 'graph', 'data', 'statistics', 'numbers', 'percentage', '图表', '数据', '统计'],
            'diagram': ['diagram', 'architecture', 'flow', 'process', 'structure', 'system', '图表', '架构', '流程'],
            'code': ['code', 'programming', 'script', 'function', 'algorithm', '代码', '编程', '脚本'],
            'image': ['image', 'picture', 'photo', 'screenshot', 'visual', '图片', '照片', '截图']
        }

        # Structure indicators
        self.structure_indicators = {
            'introduction': ['intro', 'introduction', 'background', 'overview', 'beginning', '介绍', '背景', '概述'],
            'problem': ['problem', 'challenge', 'issue', 'pain point', 'difficulty', '问题', '挑战', '痛点'],
            'solution': ['solution', 'approach', 'method', 'strategy', 'answer', '解决方案', '方法', '策略'],
            'features': ['features', 'functions', 'capabilities', 'characteristics', '功能', '特性', '特点'],
            'demo': ['demo', 'demonstration', 'example', 'case', 'showcase', '演示', '示例', '案例'],
            'conclusion': ['conclusion', 'summary', 'wrap-up', 'ending', 'final', '总结', '结束', '结论']
        }

    def analyze(self, user_input: str) -> Dict[str, Any]:
        """
        Analyze user input and return comprehensive analysis.

        Args:
            user_input: Raw user input string

        Returns:
            Dictionary containing analysis results
        """
        analysis = {
            'presentation_type': self._determine_presentation_type(user_input),
            'visual_elements': self._identify_visual_elements(user_input),
            'structure': self._extract_structure(user_input),
            'complexity': self._assess_complexity(user_input),
            'audience': self._identify_audience(user_input),
            'keywords': self._extract_keywords(user_input),
            'recommended_template': None
        }

        # Determine recommended template based on analysis
        analysis['recommended_template'] = self._recommend_template(analysis)

        return analysis

    def _determine_presentation_type(self, text: str) -> str:
        """Determine the primary presentation type."""
        scores = {}

        for ptype, keywords in self.type_keywords.items():
            score = 0
            for keyword in keywords:
                score += len(re.findall(rf'\b{re.escape(keyword)}\b', text, re.IGNORECASE))
            scores[ptype] = score

        # Return type with highest score, default to 'general'
        if max(scores.values()) == 0:
            return 'general'

        return max(scores, key=scores.get)

    def _identify_visual_elements(self, text: str) -> List[str]:
        """Identify required visual elements."""
        elements = []

        for element, keywords in self.visual_keywords.items():
            if any(keyword in text.lower() for keyword in keywords):
                elements.append(element)

        return elements

    def _extract_structure(self, text: str) -> List[Dict[str, str]]:
        """Extract presentation structure from input."""
        structure = []

        # Split by common separators
        sections = re.split(r'[,，;；\n]+', text)

        for i, section in enumerate(sections):
            section = section.strip()
            if len(section) < 3:  # Skip very short sections
                continue

            section_type = self._classify_section(section)
            structure.append({
                'index': i,
                'type': section_type,
                'content': section,
                'estimated_slides': self._estimate_slides_for_section(section_type, section)
            })

        # Ensure minimum structure
        if not structure:
            structure = [
                {'index': 0, 'type': 'introduction', 'content': 'Introduction', 'estimated_slides': 1},
                {'index': 1, 'type': 'main', 'content': 'Main Content', 'estimated_slides': 3},
                {'index': 2, 'type': 'conclusion', 'content': 'Conclusion', 'estimated_slides': 1}
            ]

        return structure

    def _classify_section(self, text: str) -> str:
        """Classify a section based on its content."""
        for stype, keywords in self.structure_indicators.items():
            if any(keyword in text.lower() for keyword in keywords):
                return stype
        return 'main'

    def _estimate_slides_for_section(self, section_type: str, content: str) -> int:
        """Estimate number of slides needed for a section."""
        base_slides = {
            'introduction': 1,
            'problem': 2,
            'solution': 3,
            'features': 2,
            'demo': 2,
            'conclusion': 1,
            'main': 2
        }

        base = base_slides.get(section_type, 2)

        # Adjust based on content length
        if len(content) > 100:
            base += 1
        if len(content) > 200:
            base += 1

        return base

    def _assess_complexity(self, text: str) -> str:
        """Assess presentation complexity."""
        complexity_score = 0

        # Length factor
        if len(text) > 500:
            complexity_score += 1
        if len(text) > 1000:
            complexity_score += 1

        # Technical content factor
        tech_keywords = self.type_keywords['technical']
        tech_count = sum(1 for keyword in tech_keywords if keyword in text.lower())
        if tech_count > 3:
            complexity_score += 1

        # Visual elements factor
        visual_count = len(self._identify_visual_elements(text))
        if visual_count > 2:
            complexity_score += 1

        if complexity_score <= 1:
            return 'basic'
        elif complexity_score <= 3:
            return 'intermediate'
        else:
            return 'advanced'

    def _identify_audience(self, text: str) -> str:
        """Identify target audience."""
        audience_keywords = {
            'executives': ['executive', 'manager', 'leader', 'ceo', 'cto', '高管', '管理者', '领导'],
            'developers': ['developer', 'programmer', 'engineer', 'technical', '开发者', '程序员', '工程师'],
            'students': ['student', 'learner', 'beginner', 'novice', '学生', '学员', '初学者'],
            'customers': ['customer', 'client', 'user', 'buyer', '客户', '用户', '消费者'],
            'investors': ['investor', 'funding', 'investment', 'venture', '投资者', '投资', '融资']
        }

        for audience, keywords in audience_keywords.items():
            if any(keyword in text.lower() for keyword in keywords):
                return audience

        return 'general'

    def _extract_keywords(self, text: str) -> List[str]:
        """Extract important keywords from text."""
        # Simple keyword extraction - can be enhanced with NLP
        words = re.findall(r'\b\w+\b', text.lower())

        # Filter out common words and keep important ones
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by',
                     '的', '是', '在', '和', '与', '或', '但是', '为了', '关于', '通过'}

        keywords = [word for word in words if word not in stop_words and len(word) > 2]

        # Return top keywords by frequency
        from collections import Counter
        keyword_counts = Counter(keywords)

        return [kw for kw, count in keyword_counts.most_common(10)]

    def _recommend_template(self, analysis: Dict[str, Any]) -> str:
        """Recommend the best template based on analysis."""
        ptype = analysis['presentation_type']
        complexity = analysis['complexity']
        visual_elements = analysis['visual_elements']

        # Base recommendation on presentation type
        template_map = {
            'business': 'business',
            'technical': 'technical',
            'education': 'education'
        }

        base_template = template_map.get(ptype, 'general')

        # Adjust based on complexity
        if complexity == 'advanced' and ptype == 'technical':
            return 'technical-advanced'

        # Adjust based on visual elements
        if 'chart' in visual_elements or 'diagram' in visual_elements:
            if base_template == 'general':
                return 'business'  # Business template handles charts well

        return base_template

def main():
    """Command line interface for the content analyzer."""
    import sys

    if len(sys.argv) != 2:
        print("Usage: python content_analyzer.py '<user input>'")
        sys.exit(1)

    user_input = sys.argv[1]
    analyzer = ContentAnalyzer()
    analysis = analyzer.analyze(user_input)

    print(json.dumps(analysis, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()