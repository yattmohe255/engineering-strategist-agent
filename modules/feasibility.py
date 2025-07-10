def fill_fel_template(project_name, opportunity, risks, roi):
    return f"""
# FEL Summary – {project_name}

**Opportunity Description:**  
{opportunity}

**Known Risks or Barriers:**  
{risks}

**Estimated ROI:**  
{roi}

**Key Assumptions:**  
- Layout is feasible for selected tech  
- Support from plant stakeholders will be secured  
- Integration timeline matches corporate targets  

**Next Steps:**  
1. Validate current process baseline  
2. Engage automation vendors  
3. Review scope with Operations, QA, Engineering  
"""