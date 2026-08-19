# Organization Profile: FinNexus Solutions

This document defines the foundational organizational context, structure, and risk profile for FinNexus Solutions. It serves as the reference point for scoping and contextualizing all security policies and procedures within the organization.

> **Portfolio status:** FinNexus Solutions is a fictional organization. The policies, registers, and mappings in this repository are illustrative drafts, not approved operating records or evidence of compliance.

## 1. Organization Overview

- **Organization Name:** FinNexus Solutions
- **Industry:** Fintech / Financial Services
- **Size:** Mid-size (~500 employees)
- **Primary Headquarters:** Mumbai, India
- **Global Operations:** Operates in India, with significant customer bases in the United States (US) and the European Union (EU).

## 2. Regulatory and Compliance Landscape

Due to its global operations and the nature of its business, FinNexus Solutions is subject to multiple regulatory frameworks:

- **India:** Digital Personal Data Protection Act (DPDP Act 2023), RBI guidelines for payment/financial institutions.
- **European Union:** General Data Protection Regulation (GDPR).
- **United States:** Various state privacy laws (e.g., CCPA/CPRA) and federal financial regulations.
- **Industry Standards:** Payment Card Industry Data Security Standard (PCI DSS) due to processing and storing payment card data.

Framework references are a scoping aid, not a legal determination of applicability or compliance. The DPDP Act and the Digital Personal Data Protection Rules, 2025 have phased commencement provisions; Legal and Compliance must confirm the obligations in force before relying on any mapped requirement.

## 3. Risk Profile

FinNexus Solutions operates with a **High Risk** profile due to the following factors:

- **Data Handled:** Processes, stores, and transmits large volumes of Personally Identifiable Information (PII) and sensitive financial/payment data.
- **Service Criticality:** Provides high-availability financial services where downtime directly impacts revenue and customer trust.
- **Threat Landscape:** As a fintech entity, it is a high-value target for financially motivated cybercriminals and ransomware operators.

## 4. Organizational Structure (Key Roles)

The organization is structured to ensure segregation of duties and robust governance:

- **Chief Information Security Officer (CISO):** Responsible for the overall security strategy, policy enforcement, and risk management. 
- **Information Technology (IT):** Manages internal systems, employee endpoints, network infrastructure, and helpdesk operations.
- **Engineering / Product Development:** Develops and maintains the core financial applications and customer-facing platforms.
- **Legal and Compliance:** Ensures all operations, products, and policies adhere to relevant laws (DPDP Act 2023, GDPR, etc.) and industry regulations.
- **Human Resources (HR):** Manages employee onboarding, offboarding, background checks, and coordinates security awareness training.

## 5. Infrastructure and Operational Assumptions

The security policies assume the following technological and operational baseline:

- **Cloud-Hosted Environment:** The primary production environment and core services are hosted on public cloud infrastructure (e.g., AWS/Azure/GCP).
- **Hybrid Workforce:** Employees operate in a hybrid model, working both from corporate offices and remote locations, utilizing company-issued devices and secure remote access solutions.
- **Third-Party Vendors:** The organization relies on various SaaS providers, third-party APIs, and managed service providers, requiring rigorous vendor risk management and supply chain security controls.
