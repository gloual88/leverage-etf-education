import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 페이지 설정
st.set_page_config(
    page_title="레버리지 ETF 이해하기",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 커스텀 CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        background: linear-gradient(90deg, #00d4ff, #7b2cbf);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        text-align: center;
        color: #888;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(145deg, #1e1e2e, #2d2d44);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.1);
    }
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
    }
    .metric-label {
        color: #888;
        font-size: 0.9rem;
    }
    .info-box {
        background: linear-gradient(90deg, rgba(123,44,191,0.2), rgba(0,212,255,0.2));
        border-left: 4px solid #7b2cbf;
        padding: 1rem;
        border-radius: 0 10px 10px 0;
        margin: 1rem 0;
    }
    .warning-box {
        background: rgba(255,71,87,0.2);
        border-left: 4px solid #ff4757;
        padding: 1rem;
        border-radius: 0 10px 10px 0;
        margin: 1rem 0;
    }
    .success-box {
        background: rgba(0,255,136,0.2);
        border-left: 4px solid #00ff88;
        padding: 1rem;
        border-radius: 0 10px 10px 0;
        margin: 1rem 0;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #1e1e2e;
        border-radius: 10px;
        padding: 10px 20px;
    }
</style>
""", unsafe_allow_html=True)

# 헤더
st.markdown('<h1 class="main-header">🎮 레버리지 ETF 완전 정복</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">KORU는 왜 예상보다 더 많이 올랐을까?</p>', unsafe_allow_html=True)

# 탭 구성
tab1, tab2, tab3, tab4 = st.tabs(["📚 개념 이해", "🎯 핵심 원리", "🎛️ 직접 실험", "📊 실제 데이터"])

# ===================== 탭 1: 개념 이해 =====================
with tab1:
    st.header("KORU가 뭔가요?")
    
    st.markdown("""
    <div class="info-box">
    <strong>KORU</strong>는 <span style="color: #00d4ff;">한국 주식시장을 3배로 따라가는</span> 미국 ETF입니다.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📈 상승할 때
        | 한국 주식 | KORU |
        |:---------:|:----:|
        | +1% | **+3%** |
        | +5% | **+15%** |
        | +10% | **+30%** |
        """)
    
    with col2:
        st.markdown("""
        ### 📉 하락할 때
        | 한국 주식 | KORU |
        |:---------:|:----:|
        | -1% | **-3%** |
        | -5% | **-15%** |
        | -10% | **-30%** |
        """)
    
    st.divider()
    
    # 2025년 결과
    st.header("🤔 2025년, 이상한 결과 발견!")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">한국 주식 (EWY)</div>
            <div class="metric-value" style="color: #3498db;">+97%</div>
            <div style="color: #888; font-size: 0.8rem;">약 2배 상승</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">단순 계산 (97% × 3)</div>
            <div class="metric-value" style="color: #f39c12;">+291%</div>
            <div style="color: #888; font-size: 0.8rem;">예상 수익률</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">KORU 실제 수익률</div>
            <div class="metric-value" style="color: #00ff88;">+447%</div>
            <div style="color: #888; font-size: 0.8rem;">약 5.5배 상승! 🚀</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box" style="text-align: center; font-size: 1.2rem;">
    🤷‍♂️ 3배짜리인데... 왜 <strong style="color: #00ff88;">156%나 더</strong> 올랐지?!
    </div>
    """, unsafe_allow_html=True)

# ===================== 탭 2: 핵심 원리 =====================
with tab2:
    st.header('🎯 핵심: "매일 3배" ≠ "1년 3배"')
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### ❌ 우리가 생각한 방식
        ```
        1년 후 = 처음 + (수익률 × 3)
        ```
        > 1년 동안의 총 수익에 3배
        """)
    
    with col2:
        st.markdown("""
        ### ✅ KORU의 실제 방식
        ```
        매일 = 어제 × (1 + 오늘수익률 × 3)
        ```
        > 매일 3배씩 복리로 굴러감!
        """)
    
    st.divider()
    
    # 눈덩이 비유
    st.header("⛄ 눈덩이로 이해하기")
    
    # 눈덩이 시각화
    snowball_data = pd.DataFrame({
        '일차': ['시작', '1일차', '2일차', '3일차', '4일차', '5일차'],
        '크기': [100, 130, 169, 220, 286, 371],
        '설명': ['100', '+30%', '+30%', '+30%', '+30%', '+30%']
    })
    
    fig_snow = go.Figure()
    
    for i, row in snowball_data.iterrows():
        fig_snow.add_trace(go.Scatter(
            x=[i],
            y=[0],
            mode='markers+text',
            marker=dict(
                size=row['크기'] / 3,
                color='#00d4ff' if i < 5 else '#00ff88',
                line=dict(width=2, color='white')
            ),
            text=f"{row['크기']}",
            textposition='middle center',
            textfont=dict(size=14, color='white'),
            showlegend=False
        ))
    
    fig_snow.update_layout(
        height=250,
        xaxis=dict(
            tickmode='array',
            tickvals=list(range(6)),
            ticktext=snowball_data['일차'].tolist(),
            showgrid=False
        ),
        yaxis=dict(visible=False, range=[-1, 1]),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=20, b=40)
    )
    
    st.plotly_chart(fig_snow, use_container_width=True)
    
    st.markdown("""
    <div class="success-box">
    💡 커진 눈덩이에 계속 3배가 적용되니까, 점점 더 빠르게 커집니다!
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # 게임 비유
    st.header("🎮 RPG 게임으로 비유하면")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### ⚔️ 버프 A: 단순 3배
        게임 끝날 때 총 데미지의 3배 보너스
        
        ```
        턴1: 10 → 턴2: 10 → 턴3: 10
        총 30 × 3 = 90
        ```
        """)
    
    with col2:
        st.markdown("""
        ### ⚡ 버프 B: 매턴 3배 (KORU 방식)
        매 턴마다 공격력 3배 적용!
        
        ```
        턴1: 30 → 턴2: 30 → 턴3: 30
        총 90 (+ 복리효과!)
        ```
        """)
    
    st.info("당연히 **버프 B**가 훨씬 강력하겠죠? KORU는 **버프 B** 방식입니다! 🎯")

# ===================== 탭 3: 직접 실험 =====================
with tab3:
    st.header("🎛️ 직접 실험해보기")
    st.markdown("슬라이더를 움직여서 다양한 상황을 실험해보세요!")
    
    st.divider()
    
    # 시뮬레이터 컨트롤
    col1, col2, col3 = st.columns(3)
    
    with col1:
        day1 = st.slider("1일차 수익률 (%)", -30, 30, 10, key="day1")
    with col2:
        day2 = st.slider("2일차 수익률 (%)", -30, 30, 10, key="day2")
    with col3:
        day3 = st.slider("3일차 수익률 (%)", -30, 30, 10, key="day3")
    
    # 계산
    d1, d2, d3 = day1/100, day2/100, day3/100
    
    # 기초자산 계산
    base_values = [100]
    base_values.append(base_values[-1] * (1 + d1))
    base_values.append(base_values[-1] * (1 + d2))
    base_values.append(base_values[-1] * (1 + d3))
    base_return = base_values[-1] - 100
    
    # 단순 3배
    simple_return = base_return * 3
    
    # 레버리지 3배
    lev_values = [100]
    lev_values.append(lev_values[-1] * (1 + d1 * 3))
    lev_values.append(lev_values[-1] * (1 + d2 * 3))
    lev_values.append(lev_values[-1] * (1 + d3 * 3))
    lev_return = lev_values[-1] - 100
    
    # 괴리율
    diff = lev_return - simple_return
    
    st.divider()
    
    # 결과 표시
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        color = "#3498db" if base_return >= 0 else "#ff4757"
        st.metric(
            label="기초자산 수익률",
            value=f"{base_return:+.1f}%",
            delta=None
        )
    
    with col2:
        color = "#f39c12" if simple_return >= 0 else "#ff4757"
        st.metric(
            label="단순 3배 (예상)",
            value=f"{simple_return:+.1f}%",
            delta=None
        )
    
    with col3:
        color = "#00ff88" if lev_return >= 0 else "#ff4757"
        st.metric(
            label="레버리지 3배 (실제)",
            value=f"{lev_return:+.1f}%",
            delta=f"{diff:+.1f}%p 괴리"
        )
    
    with col4:
        if diff > 0:
            st.success(f"🚀 복리 부스트!\n+{diff:.1f}%p 추가 수익")
        elif diff < 0:
            st.error(f"📉 변동성 손실!\n{diff:.1f}%p 손실")
        else:
            st.info("차이 없음")
    
    # 시각화
    fig = make_subplots(rows=1, cols=2, subplot_titles=("일별 가격 추이", "최종 수익률 비교"))
    
    days_label = ['시작', '1일차', '2일차', '3일차']
    
    # 가격 추이 차트
    fig.add_trace(
        go.Scatter(x=days_label, y=base_values, name='기초자산', 
                   line=dict(color='#3498db', width=3), mode='lines+markers'),
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(x=days_label, y=lev_values, name='레버리지 3배',
                   line=dict(color='#00ff88', width=3), mode='lines+markers'),
        row=1, col=1
    )
    
    # 수익률 비교 바 차트
    fig.add_trace(
        go.Bar(
            x=['기초자산', '단순 3배', '레버리지 3배'],
            y=[base_return, simple_return, lev_return],
            marker_color=['#3498db', '#f39c12', '#00ff88'],
            text=[f'{base_return:.1f}%', f'{simple_return:.1f}%', f'{lev_return:.1f}%'],
            textposition='outside',
            showlegend=False
        ),
        row=1, col=2
    )
    
    fig.update_layout(
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        legend=dict(orientation='h', yanchor='bottom', y=1.02)
    )
    
    fig.update_xaxes(gridcolor='rgba(255,255,255,0.1)')
    fig.update_yaxes(gridcolor='rgba(255,255,255,0.1)')
    
    st.plotly_chart(fig, use_container_width=True)
    
    # 상세 테이블
    st.subheader("📋 상세 계산 과정")
    
    detail_df = pd.DataFrame({
        '': ['시작', '1일차', '2일차', '3일차', '최종 수익률'],
        '일일 수익률': ['-', f'{day1:+}%', f'{day2:+}%', f'{day3:+}%', '-'],
        '기초자산': [f'{base_values[0]:.1f}', f'{base_values[1]:.1f}', f'{base_values[2]:.1f}', f'{base_values[3]:.1f}', f'{base_return:+.1f}%'],
        '레버리지 3배': [f'{lev_values[0]:.1f}', f'{lev_values[1]:.1f}', f'{lev_values[2]:.1f}', f'{lev_values[3]:.1f}', f'{lev_return:+.1f}%']
    })
    
    st.dataframe(detail_df, use_container_width=True, hide_index=True)
    
    st.divider()
    
    # 프리셋 시나리오
    st.subheader("🎬 시나리오 프리셋")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📈 꾸준한 상승장", use_container_width=True):
            st.session_state.day1 = 10
            st.session_state.day2 = 10
            st.session_state.day3 = 10
            st.rerun()
    
    with col2:
        if st.button("🎢 롤러코스터 (횡보)", use_container_width=True):
            st.session_state.day1 = 15
            st.session_state.day2 = -15
            st.session_state.day3 = 15
            st.rerun()
    
    with col3:
        if st.button("📉 꾸준한 하락장", use_container_width=True):
            st.session_state.day1 = -10
            st.session_state.day2 = -10
            st.session_state.day3 = -10
            st.rerun()

# ===================== 탭 4: 실제 데이터 =====================
with tab4:
    st.header("📊 2025년 실제 데이터 분석")
    
    # 실제 데이터 시뮬레이션 (250거래일)
    np.random.seed(42)
    days = 250
    
    # 연간 97% 수익률을 일일로 환산 + 변동성
    daily_mean = np.log(1.97) / days
    daily_vol = 0.015
    
    daily_returns = np.random.normal(daily_mean, daily_vol, days)
    
    # 가격 계산
    base_price = [100]
    leverage_price = [100]
    
    for r in daily_returns:
        base_price.append(base_price[-1] * np.exp(r))
        leverage_price.append(leverage_price[-1] * (1 + (np.exp(r) - 1) * 3))
    
    # 단순 3배 선
    final_base_return = (base_price[-1] / 100 - 1)
    simple_3x = [100 + (final_base_return * 3 * 100 * i / days) for i in range(days + 1)]
    
    # 차트
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        y=base_price,
        name='EWY (한국주식)',
        line=dict(color='#3498db', width=2)
    ))
    
    fig.add_trace(go.Scatter(
        y=simple_3x,
        name='단순 3배 예상',
        line=dict(color='#f39c12', width=2, dash='dash')
    ))
    
    fig.add_trace(go.Scatter(
        y=leverage_price,
        name='KORU (매일 3배 복리)',
        line=dict(color='#00ff88', width=2)
    ))
    
    fig.update_layout(
        title='2025년 연간 수익률 비교',
        xaxis_title='거래일',
        yaxis_title='가격',
        height=500,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        legend=dict(orientation='h', yanchor='bottom', y=1.02)
    )
    
    fig.update_xaxes(gridcolor='rgba(255,255,255,0.1)')
    fig.update_yaxes(gridcolor='rgba(255,255,255,0.1)')
    
    st.plotly_chart(fig, use_container_width=True)
    
    # 결과 요약
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("EWY 수익률", f"{(base_price[-1]/100-1)*100:.1f}%")
    with col2:
        st.metric("단순 3배", f"{(base_price[-1]/100-1)*300:.1f}%")
    with col3:
        st.metric("KORU 실제", f"{(leverage_price[-1]/100-1)*100:.1f}%", 
                  delta=f"{(leverage_price[-1]/100-1)*100 - (base_price[-1]/100-1)*300:.1f}%p")
    
    st.divider()
    
    # 경고 섹션
    st.header("⚠️ 주의! 항상 좋은 건 아니에요")
    
    st.markdown("""
    <div class="warning-box">
    2025년은 한국 주식이 <strong>꾸준히 올랐기 때문에</strong> 이런 결과가 나왔습니다.<br>
    만약 오르락내리락 반복했다면 <strong style="color: #ff4757;">변동성 손실</strong>이 발생합니다!
    </div>
    """, unsafe_allow_html=True)
    
    # 상승장 vs 횡보장 비교
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 상승장 시나리오")
        up_base = [100]
        up_lev = [100]
        for _ in range(10):
            up_base.append(up_base[-1] * 1.05)
            up_lev.append(up_lev[-1] * 1.15)
        
        fig_up = go.Figure()
        fig_up.add_trace(go.Scatter(y=up_base, name='기초자산', line=dict(color='#3498db')))
        fig_up.add_trace(go.Scatter(y=up_lev, name='레버리지 3배', line=dict(color='#00ff88')))
        fig_up.update_layout(height=300, showlegend=True,
                            plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_up, use_container_width=True)
        st.success(f"기초자산: +{(up_base[-1]/100-1)*100:.0f}% → 레버리지: +{(up_lev[-1]/100-1)*100:.0f}%")
    
    with col2:
        st.subheader("🎢 횡보장 시나리오")
        side_base = [100]
        side_lev = [100]
        pattern = [0.1, -0.09, 0.08, -0.07, 0.1, -0.09, 0.08, -0.07, 0.05, -0.04]
        for p in pattern:
            side_base.append(side_base[-1] * (1 + p))
            side_lev.append(side_lev[-1] * (1 + p * 3))
        
        fig_side = go.Figure()
        fig_side.add_trace(go.Scatter(y=side_base, name='기초자산', line=dict(color='#f39c12')))
        fig_side.add_trace(go.Scatter(y=side_lev, name='레버리지 3배', line=dict(color='#ff4757')))
        fig_side.update_layout(height=300, showlegend=True,
                              plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_side, use_container_width=True)
        st.error(f"기초자산: {(side_base[-1]/100-1)*100:+.0f}% → 레버리지: {(side_lev[-1]/100-1)*100:+.0f}%")

# 푸터
st.divider()

st.markdown("""
<div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, rgba(123,44,191,0.2), rgba(0,212,255,0.2)); border-radius: 15px; margin-top: 2rem;">
    <h3>📝 한 줄 요약</h3>
    <p style="font-size: 1.1rem; line-height: 1.8;">
        KORU는 <strong style="color: #00ff88;">매일 3배씩 복리로 굴러가기</strong> 때문에,<br><br>
        📈 꾸준히 오르는 시장에서는 <strong style="color: #00ff88;">3배보다 훨씬 많이</strong> 오르고,<br>
        📉 오르락내리락하면 <strong style="color: #ff4757;">3배보다 훨씬 많이 손해</strong>봅니다.
    </p>
</div>
""", unsafe_allow_html=True)

st.caption("Made with ❤️ for Financial Education")