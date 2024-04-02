import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Mingheng Wu",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="auto",
)

# Header
st.title("Mingheng Wu")

# Contact Info
st.markdown("""
**Contact Information**  
📞 (+1) 206 756 xxxx  
✉️ [wmhst7@gmail.com](mailto:wmhst7@gmail.com)  
🏛️ [University of Washington](https://www.washington.edu/) | [Tsinghua University](http://www.tsinghua.edu.cn)  
🔗 [LinkedIn](https://www.linkedin.com/in/minghengwu/) | [GitHub](https://github.com/wmhst7)  
""")

# Profile Section
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("""
    ## Education
    - **Master of Science, GIX** (Dual Degree)  
      University of Washington  
      Sep 2023 – Mar 2025
      
    - **Master of Science, GIX** (Dual Degree)  
      Tsinghua University  
      Sep 2022 – Mar 2025
      
    - **Bachelor of Engineer in Computer Science and Technology**  
      Tsinghua University  
      Aug 2018 – Jun 2022
      
    """)
with col2:
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/5/58/University_of_Washington_seal.svg/1920px-University_of_Washington_seal.svg.png", width=200)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Tsinghua_University_Logo.svg/1920px-Tsinghua_University_Logo.svg.png", width=200)

# Work Experience
st.markdown("""
## Work Experience
            
**ByteDance AML**  
_Incoming Research Engineer Intern_  
Jun 2024 - Sep 2024  
- Machine Learning System focuing on LLM systems.

**Metabit Trading**  
_Software Engineer Intern_  
Jun 2023 - Sep 2023  
- Engineered and deployed optimization to enhance stability and availability on company’s Authorization Service.

**Microsoft**  
_Software Engineer Intern_  
Mar 2023 - May 2023  
- Contributed to natural language generation model used in Microsoft Bing. Optimized inference latency based on FasterTransformer and enhanced performance by experiments on MoE architecture.

**Microsoft Research**  
_Research Engineer Intern_  
Nov 2021 - May 2022  
- At MSRA. Devised and implemented a framework which can adaptively adjust the three indicators of model complexity, image compression rate, and image quality based on a learned video compression model.
- Integrated GAN into a video compression model aimed at enhancing subjective image quality, mitigating the influence of adverse image objective indicators on the model.

**Disney+ Hotstar**  
_Software Engineer Intern_  
Jun 2021 - Sep 2021  
- Engineered a video coding pipeline to optimize movie transmission efficiency, employing a multifaceted strategy.

**Peking University Artificial Intelligence Innovation Center**  
_Research Engineer Intern_  
Jan 2021 - Jun 2021  
- Contributed to developing a pose estimation model and an error correction model for home fitness scenarios.
""")

# Projects Section
st.markdown("""
## Projects

- **Efficient Extraction of Nailfold Microcirculation Features from Images**  
  Feb 2022 - Aug 2022  
  Computer Vision in Medical Area: Developed an advanced framework employing U-Net and other cutting-edge methods for precise detection, segmentation, and feature extraction of nailfold microcirculation capillaries.

- **Five Stage Pipeline CPU based on RISC-V**  
  Sep 2020 - Jan 2022  
  Using Verilog to implement a complete five-stage pipeline CPU design and development based on FPGA. It supports 30 instructions and functions including interrupt, exception, page table, and TLB. A simple shell could run on it.
""")

# Footer
footer = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #f1f1f1;
    color: grey;
    text-align: center;
    padding: 10px;
}
</style>

<div class="footer">
  <p>Made with ❤️ in Streamlit by Mingheng Wu</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
