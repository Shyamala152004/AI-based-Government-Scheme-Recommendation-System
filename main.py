from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="SchemeAI API",
    description="Backend API for National Welfare Scheme Navigator",
    version="1.0.0"
)

# Enable CORS for Frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic Models for Request Validation
class UserProfile(BaseModel):
    age: int
    gender: str
    income: float
    state: str
    category: str
    occupation: str

class SchemeCreate(BaseModel):
    name: str
    category: str
    max_income: float
    official_url: str
    description: str

class ChatMessage(BaseModel):
    message: str

# ==================== COMPREHENSIVE SCHEMES DATASET (200 Schemes) ====================
ALL_SCHEMES = [
    # --- EDUCATION SCHEMES (1 to 50) ---
    {
        "id": 1, "name": "National Scholarship Portal (NSP) Central Sector Scheme", "category": "Education",
        "max_income": 450000, "official_url": "https://scholarships.gov.in",
        "description": "Financial assistance to meritorious students from low-income families to meet day-to-day expenses while pursuing higher studies."
    },
    {
        "id": 2, "name": "PM Young Achievers Scholarship Scheme (PM-YASASVI)", "category": "Education",
        "max_income": 250000, "official_url": "https://socialjustice.gov.in",
        "description": "Scholarships for OBC, EBC, and DNT students studying in top-class schools across India."
    },
    {
        "id": 3, "name": "AICTE Pragati Scholarship for Girls", "category": "Education",
        "max_income": 800000, "official_url": "https://www.aicte-india.org",
        "description": "Providing financial support of ₹50,000 per annum to girl students pursuing technical degree or diploma courses."
    },
    {
        "id": 4, "name": "AICTE Saksham Scholarship for Differently-Abled", "category": "Education",
        "max_income": 800000, "official_url": "https://www.aicte-india.org",
        "description": "Special scholarship scheme for specially-abled students pursuing technical education at AICTE approved institutions."
    },
    {
        "id": 5, "name": "National Means-cum-Merit Scholarship (NMMSS)", "category": "Education",
        "max_income": 350000, "official_url": "https://scholarships.gov.in",
        "description": "Scholarships awarded to meritorious students of economically weaker sections to arrest dropouts at class 8 level."
    },
    {
        "id": 6, "name": "Post Matric Scholarship for SC Students", "category": "Education",
        "max_income": 250000, "official_url": "https://scholarships.gov.in",
        "description": "Financial assistance to Scheduled Caste students studying at post matriculation or post secondary stage."
    },
    {
        "id": 7, "name": "Post Matric Scholarship for ST Students", "category": "Education",
        "max_income": 250000, "official_url": "https://scholarships.gov.in",
        "description": "Enabling ST students to complete their education with maintenance allowance and fee reimbursements."
    },
    {
        "id": 8, "name": "Post Matric Scholarship for OBC Students", "category": "Education",
        "max_income": 150000, "official_url": "https://scholarships.gov.in",
        "description": "Financial aid for Other Backward Class students for pursuing higher education studies."
    },
    {
        "id": 9, "name": "Maulana Azad National Fellowship for Minority Students", "category": "Education",
        "max_income": 600000, "official_url": "https://www.minorityaffairs.gov.in",
        "description": "Integrated five-year fellowship scheme for higher education research leading to M.Phil/Ph.D degrees."
    },
    {
        "id": 10, "name": "INSPIRE Scholarship for Higher Education (SHE)", "category": "Education",
        "max_income": 500000, "official_url": "https://online-inspire.gov.in",
        "description": "Attracting talented youth to study natural and basic sciences by offering ₹80,000 per year."
    },
    {
        "id": 11, "name": "Prime Minister's Research Fellowship (PMRF)", "category": "Education",
        "max_income": 1000000, "official_url": "https://pmrf.in",
        "description": "Attracting the best talent for research in premier higher educational institutions in India with heavy stipends."
    },
    {
        "id": 12, "name": "Central Sector Scheme of Scholarship for College and University Students", "category": "Education",
        "max_income": 450000, "official_url": "https://scholarships.gov.in",
        "description": "Financial support to upper secondary school students belonging to low-income families."
    },
    {
        "id": 13, "name": "Ishanya Scholarship for North Eastern Region", "category": "Education",
        "max_income": 600000, "official_url": "https://scholarships.gov.in",
        "description": "Special educational grant for students originating from North Eastern states."
    },
    {
        "id": 14, "name": "BEGSS - Begum Hazrat Mahal National Scholarship", "category": "Education",
        "max_income": 200000, "official_url": "https://scholarships.gov.in",
        "description": "Merit-cum-means scholarship for meritorious girl students belonging to minority communities."
    },
    {
        "id": 15, "name": "Vidya Lakshmi Education Loan Portal Scheme", "category": "Education",
        "max_income": 1200000, "official_url": "https://www.vidyalakshmi.co.in",
        "description": "Single-window electronic portal for students seeking education loans across Indian banks."
    },
    {
        "id": 16, "name": "National Fellowship and Scholarship for Higher Education of ST Students", "category": "Education",
        "max_income": 600000, "official_url": "https://scholarships.gov.in",
        "description": "Financial assistance for ST students pursuing M.Phil, Ph.D and specialized higher degrees."
    },
    {
        "id": 17, "name": "Dr. Ambedkar Central Sector Scheme of Interest Subsidy on Educational Loans", "category": "Education",
        "max_income": 800000, "official_url": "https://socialjustice.gov.in",
        "description": "Full interest subsidy during moratorium period on education loans for studies abroad for OBC and EBC students."
    },
    {
        "id": 18, "name": "Padho Pardes Scheme for Overseas Studies", "category": "Education",
        "max_income": 600000, "official_url": "https://www.minorityaffairs.gov.in",
        "description": "Interest subsidy on education loans for minority students pursuing Masters and Ph.D abroad."
    },
    {
        "id": 19, "name": "Pradhan Mantri Kaushal Vikas Yojana (PMKVY) Skill Training", "category": "Education",
        "max_income": 500000, "official_url": "https://www.pmkviyo.org",
        "description": "Industry-relevant skill training and certification scheme for youth with monetary rewards."
    },
    {
        "id": 20, "name": "UGC Post-Graduate Indira Gandhi Scholarship for Single Girl Child", "category": "Education",
        "max_income": 1000000, "official_url": "https://www.ugc.ac.in",
        "description": "Promoting higher education for single girl children who happen to be the only child in their families."
    },
    {
        "id": 21, "name": "UGC Post Graduate Merit Scholarship for University Rank Holders", "category": "Education",
        "max_income": 800000, "official_url": "https://www.ugc.ac.in",
        "description": "Encouraging meritorious undergraduate students to pursue postgraduate studies in universities."
    },
    {
        "id": 22, "name": "CSIR Innovation Fellowship for School Children", "category": "Education",
        "max_income": 400000, "official_url": "https://www.csir.res.in",
        "description": "Promoting scientific creativity, innovation, and technological project building among young students."
    },
    {
        "id": 23, "name": "AICTE Swanath Scholarship Scheme", "category": "Education",
        "max_income": 800000, "official_url": "https://www.aicte-india.org",
        "description": "Financial support of ₹50,000 per annum for orphans, wards of armed forces killed in action, and COVID-affected students."
    },
    {
        "id": 24, "name": "National Talent Search Examination (NTSE) Scholarship", "category": "Education",
        "max_income": 500000, "official_url": "https://ncert.nic.in",
        "description": "Prestigious scholarship program identifying and nurturing talented secondary school students."
    },
    {
        "id": 25, "name": "Kishore Vaigyanik Protsahan Yojana (KVPY) Successor Fellowship", "category": "Education",
        "max_income": 1000000, "official_url": "https://www.iisc.ac.in",
        "description": "Encouraging students to take up research careers in science, engineering, and medicine."
    },
    {
        "id": 26, "name": "Satyendra Nath Bose National Fellowship for Science Students", "category": "Education",
        "max_income": 600000, "official_url": "https://dst.gov.in",
        "description": "Summer research fellowships for bright undergraduate students in premier national science laboratories."
    },
    {
        "id": 27, "name": "Prime Minister’s Special Scholarship Scheme (PMSSS) for J&K and Ladakh", "category": "Education",
        "max_income": 800000, "official_url": "https://www.aicte-india.org",
        "description": "Building academic capacity and providing higher education opportunities for youth in Jammu & Kashmir and Ladakh."
    },
    {
        "id": 28, "name": "Pre-Matric Scholarship for SC Students", "category": "Education",
        "max_income": 250000, "official_url": "https://scholarships.gov.in",
        "description": "Financial support for Scheduled Caste students studying in classes 9 and 10 to prevent school dropouts."
    },
    {
        "id": 29, "name": "Pre-Matric Scholarship for ST Students", "category": "Education",
        "max_income": 200000, "official_url": "https://scholarships.gov.in",
        "description": "Scholarship grant for ST students at the pre-matriculation stage to support basic education."
    },
    {
        "id": 30, "name": "Pre-Matric Scholarship for Minority Communities", "category": "Education",
        "max_income": 100000, "official_url": "https://scholarships.gov.in",
        "description": "Assistance to school students from minority communities for school tuition and stationary fees."
    },
    {
        "id": 31, "name": "Merit-cum-Means Scholarship for Professional and Technical Courses", "category": "Education",
        "max_income": 250000, "official_url": "https://scholarships.gov.in",
        "description": "Professional degree course fee support for students from minority communities."
    },
    {
        "id": 32, "name": "National Overseas Scholarship for SC Students", "category": "Education",
        "max_income": 800000, "official_url": "https://socialjustice.gov.in",
        "description": "Financial assistance to selected SC students for pursuing Master's and Ph.D degrees abroad."
    },
    {
        "id": 33, "name": "National Overseas Scholarship for ST Students", "category": "Education",
        "max_income": 600000, "official_url": "https://tribal.nic.in",
        "description": "Funding higher education abroad in foreign universities for eligible Scheduled Tribe scholars."
    },
    {
        "id": 34, "name": "Rajiv Gandhi National Fellowship for SC Students", "category": "Education",
        "max_income": 800000, "official_url": "https://socialjustice.gov.in",
        "description": "Providing doctoral research fellowships to SC candidates enrolled in universities."
    },
    {
        "id": 35, "name": "DBT Star College Scheme for Undergraduate Education", "category": "Education",
        "max_income": 1000000, "official_url": "https://dbtindia.gov.in",
        "description": "Enhancing undergraduate science education quality and laboratory equipment grants in colleges."
    },
    {
        "id": 36, "name": "AICTE IDEA Lab Educational Initiative", "category": "Education",
        "max_income": 1000000, "official_url": "https://www.aicte-india.org",
        "description": "Empowering students with hands-on multidisciplinary engineering innovation spaces."
    },
    {
        "id": 37, "name": "NPTEL Online Certification Fee Subsidy Scheme", "category": "Education",
        "max_income": 500000, "official_url": "https://nptel.ac.in",
        "description": "Reimbursement of online examination and certification fees for deserving engineering and science students."
    },
    {
        "id": 38, "name": "ICMR Junior Research Fellowship in Biomedical Sciences", "category": "Education",
        "max_income": 800000, "official_url": "https://icmr.nic.in",
        "description": "Research fellowships for medical and life science graduates pursuing doctoral studies."
    },
    {
        "id": 39, "name": "CSIR-UGC NET Junior Research Fellowship (JRF)", "category": "Education",
        "max_income": 1000000, "official_url": "https://csirhrdg.res.in",
        "description": "Monthly stipend and contingency grant for science researchers qualifying national eligibility tests."
    },
    {
        "id": 40, "name": "ICAR National Talent Scholarship in Agriculture", "category": "Education",
        "max_income": 600000, "official_url": "https://icar.org.in",
        "description": "Scholarships for students pursuing bachelor's degrees in agriculture and allied sciences."
    },
    {
        "id": 41, "name": "National Education Society for Tribal Students (NESTS) Grant", "category": "Education",
        "max_income": 300000, "official_url": "https://tribal.nic.in",
        "description": "Educational support and boarding grants for Eklavya Model Residential Schools (EMRS)."
    },
    {
        "id": 42, "name": "CBSE Single Girl Child Scholarship Scheme", "category": "Education",
        "max_income": 600000, "official_url": "https://www.cbse.gov.in",
        "description": "Encouraging parents to promote girl education and providing financial support for class 11 and 12 studies."
    },
    {
        "id": 43, "name": "AICTE-LILAVATI Award Educational Grant", "category": "Education",
        "max_income": 1000000, "official_url": "https://www.aicte-india.org",
        "description": "Grants and recognition for women empowerment initiatives in higher education institutes."
    },
    {
        "id": 44, "name": "DST Women Scientist Scheme (WOS-A)", "category": "Education",
        "max_income": 800000, "official_url": "https://dst.gov.in",
        "description": "Fellowships for women scientists and technologists having a break in career to pursue research."
    },
    {
        "id": 45, "name": "SPARK Summer Research Fellowship for Engineering Students", "category": "Education",
        "max_income": 800000, "official_url": "https://spark.iitr.ac.in",
        "description": "Research fellowships for undergraduate engineering students to work on cutting-edge projects."
    },
    {
        "id": 46, "name": "National Initiative for School Heads and Teachers Holistic Advancement", "category": "Education",
        "max_income": 1000000, "official_url": "https://itpd.ncert.gov.in",
        "description": "Capacity building and pedagogical training grants for educators across India."
    },
    {
        "id": 47, "name": "PM SHRI Schools Upgradation Grant", "category": "Education",
        "max_income": 1000000, "official_url": "https://pmshri.education.gov.in",
        "description": "Development of model schools showcasing all components of the National Education Policy (NEP)."
    },
    {
        "id": 48, "name": "Samagra Shiksha Teacher Development and Student Grant", "category": "Education",
        "max_income": 500000, "official_url": "https://samagra.education.gov.in",
        "description": "Integrated school education scheme providing free textbooks, uniforms, and learning aids."
    },
    {
        "id": 49, "name": "Atal Tinkering Lab (ATL) Grant for Schools", "category": "Education",
        "max_income": 1000000, "official_url": "https://aim.gov.in",
        "description": "Establishing innovation workspaces equipped with 3D printers and robotics kits in high schools."
    },
    {
        "id": 50, "name": "National Digital Library of India (NDLI) Club Grant", "category": "Education",
        "max_income": 1000000, "official_url": "https://ndl.iitkgp.ac.in",
        "description": "Promoting digital literacy and virtual library resource access across academic institutions."
    },

    # --- HOUSING SCHEMES (51 to 100) ---
    {
        "id": 51, "name": "Pradhan Mantri Awas Yojana - Urban (PMAY-U)", "category": "Housing",
        "max_income": 1800000, "official_url": "https://pmaymis.gov.in",
        "description": "Credit Linked Subsidy Scheme (CLSS) providing interest subsidies on home loans for EWS, LIG, and MIG families."
    },
    {
        "id": 52, "name": "Pradhan Mantri Awas Yojana - Gramin (PMAY-G)", "category": "Housing",
        "max_income": 300000, "official_url": "https://pmayg.nic.in",
        "description": "Financial assistance of up to ₹1.5 Lakhs for rural homeless families to construct pucca houses."
    },
    {
        "id": 53, "name": "Affordable Rental Housing Complexes (ARHC)", "category": "Housing",
        "max_income": 600000, "official_url": "https://pmaymis.gov.in",
        "description": "Providing ease of living for urban migrants and poor by creating affordable rental housing near workplaces."
    },
    {
        "id": 54, "name": "Rajiv Awas Yojana (RAY) Modernization Scheme", "category": "Housing",
        "max_income": 400000, "official_url": "https://mohua.gov.in",
        "description": "Slum-free India vision providing property rights, civic infrastructure, and decent housing units."
    },
    {
        "id": 55, "name": "Deendayal Antyodaya Yojana Housing Grant", "category": "Housing",
        "max_income": 250000, "official_url": "https://aayush.gov.in",
        "description": "Subsidized construction and urban habitat support for marginalized community workers."
    },
    {
        "id": 56, "name": "Indira Awas Rehabilitation Housing Scheme", "category": "Housing",
        "max_income": 200000, "official_url": "https://rural.nic.in",
        "description": "Housing grants for disaster-affected and displaced rural families."
    },
    {
        "id": 57, "name": "State Government Free Housing Patta Scheme", "category": "Housing",
        "max_income": 150000, "official_url": "https://www.myscheme.gov.in",
        "description": "Issuance of land titles (Pattas) and financial aid for roof construction for landless poor."
    },
    {
        "id": 58, "name": "Green Housing Subsidy Initiative", "category": "Housing",
        "max_income": 800000, "official_url": "https://beeindia.gov.in",
        "description": "Special incentives and interest rebates for eco-friendly and solar-integrated sustainable residential buildings."
    },
    {
        "id": 59, "name": "National Urban Housing Fund Interest Subvention Scheme", "category": "Housing",
        "max_income": 1200000, "official_url": "https://nhb.org.in",
        "description": "Subsidized term loans for housing developers and home buyers in tier-2 and tier-3 cities."
    },
    {
        "id": 60, "name": "Chief Minister Rural Housing Mission", "category": "Housing",
        "max_income": 350000, "official_url": "https://www.myscheme.gov.in",
        "description": "State-backed financial grants for constructing earthquake-resistant rural homes."
    },
    {
        "id": 61, "name": "Slum Redevelopment and Rehabilitation Scheme", "category": "Housing",
        "max_income": 300000, "official_url": "https://mohua.gov.in",
        "description": "In-situ rehabilitation of slum dwellers using land as a resource with private builder participation."
    },
    {
        "id": 62, "name": "Vajpayee Urban Housing Scheme", "category": "Housing",
        "max_income": 500000, "official_url": "https://www.myscheme.gov.in",
        "description": "Affordable housing finance for lower-income group families in urban municipal limits."
    },
    {
        "id": 63, "name": "Colony Infrastructure and Water Connection Grant", "category": "Housing",
        "max_income": 400000, "official_url": "https://amrut.gov.in",
        "description": "Providing piped water supply, sewerage, and electricity connections to newly allotted welfare housing colonies."
    },
    {
        "id": 64, "name": "Solar Rooftop Integration Housing Subsidy", "category": "Housing",
        "max_income": 1000000, "official_url": "https://solarrooftop.gov.in",
        "description": "Capital subsidy for installing solar panels on residential rooftops to reduce electricity bills."
    },
    {
        "id": 65, "name": "NABARD Rural Housing Direct Finance Scheme", "category": "Housing",
        "max_income": 400000, "official_url": "https://www.nabard.org",
        "description": "Refinancing and direct credit for building robust dwelling units in remote rural areas."
    },
    {
        "id": 66, "name": " Ambedkar Hastshilp Vikas Yojana Housing Support", "category": "Housing",
        "max_income": 250000, "official_url": "https://handicrafts.nic.in",
        "description": "Special housing and workshed construction grants for registered national awardee artisans."
    },
    {
        "id": 67, "name": "Beedi Workers Housing Subsidy Scheme", "category": "Housing",
        "max_income": 200000, "official_url": "https://labour.gov.in",
        "description": "Financial assistance for beedi workers to build hygienic residential houses."
    },
    {
        "id": 68, "name": "Cine Workers Housing Grant", "category": "Housing",
        "max_income": 300000, "official_url": "https://labour.gov.in",
        "description": "Housing assistance subsidy for low-wage cine workers across film production hubs."
    },
    {
        "id": 69, "name": "Mine Workers Welfare Housing Scheme", "category": "Housing",
        "max_income": 350000, "official_url": "https://labour.gov.in",
        "description": "Subsidized housing loans and construction grants for iron, manganese, and limestone mine workers."
    },
    {
        "id": 70, "name": "Handloom Weaver Shed and Housing Scheme", "category": "Housing",
        "max_income": 250000, "official_url": "https://handlooms.nic.in",
        "description": "Combined workshed and residential housing grant for traditional handloom weavers."
    },
    {
        "id": 71, "name": "Fishermen Model Housing Scheme", "category": "Housing",
        "max_income": 250000, "official_url": "https://dof.gov.in",
        "description": "Building coastal housing units with storm protection for active marine fishermen families."
    },
    {
        "id": 72, "name": "Safai Karamchari Rehabilitation Housing Grant", "category": "Housing",
        "max_income": 300000, "official_url": "https://nsKFDC.nic.in",
        "description": "Special financial packages including housing grants for liberated manual scavengers."
    },
    {
        "id": 73, "name": "Pradhan Mantri Jan Awas Credit Guarantee Scheme", "category": "Housing",
        "max_income": 600000, "official_url": "https://pmaymis.gov.in",
        "description": "Credit guarantees to primary lending institutions for unsecured housing loans to weaker sections."
    },
    {
        "id": 74, "name": "TCPO Urban Shelter Upgradation Programme", "category": "Housing",
        "max_income": 400000, "official_url": "https://mohua.gov.in",
        "description": "Upgradation of semi-pucca houses into durable concrete homes in urban pockets."
    },
    {
        "id": 75, "name": "Nirmal Bharat Abhiyan Sanitation and Toilet Housing Grant", "category": "Housing",
        "max_income": 300000, "official_url": "https://swachhbharatmission.ddws.gov.in",
        "description": "Incentive grant for constructing individual household latrines attached to residential units."
    },
    {
        "id": 76, "name": "National Housing Bank Low-Income Shelter Fund", "category": "Housing",
        "max_income": 500000, "official_url": "https://nhb.org.in",
        "description": "Low-interest financial assistance to housing cooperatives and micro-finance institutions."
    },
    {
        "id": 77, "name": "North-East Rural Housing Development Assistance", "category": "Housing",
        "max_income": 400000, "official_url": "https://mdoner.gov.in",
        "description": "Special housing construction subsidies suited for hilly and heavy rainfall terrains in the North-East."
    },
    {
        "id": 78, "name": "Disaster Resilient Housing Reconstruction Scheme", "category": "Housing",
        "max_income": 500000, "official_url": "https://ndma.gov.in",
        "description": "Grants to rebuild flood, cyclone, and earthquake-damaged houses with modern resilient standards."
    },
    {
        "id": 79, "name": "Ex-Servicemen Contributory Housing Grant", "category": "Housing",
        "max_income": 800000, "official_url": "https://ksb.gov.in",
        "description": "Financial assistance for retired defense personnel to build or repair residential houses."
    },
    {
        "id": 80, "name": "Widow Housing Assistance Welfare Scheme", "category": "Housing",
        "max_income": 200000, "official_url": "https://socialjustice.gov.in",
        "description": "Priority housing allotment and cash assistance for destitute widows."
    },
    {
        "id": 81, "name": "Divyangjan Accessible Housing Modification Grant", "category": "Housing",
        "max_income": 400000, "official_url": "https://socialjustice.gov.in",
        "description": "Grants to modify residential homes with ramps, railings, and accessible restrooms for persons with disabilities."
    },
    {
        "id": 82, "name": "State Housing Board Affordable Plot Scheme", "category": "Housing",
        "max_income": 600000, "official_url": "https://www.myscheme.gov.in",
        "description": "Subsidized residential land plots allotted through lottery draws to economically weaker sections."
    },
    {
        "id": 83, "name": "Rental Housing Vouchers for Migrant Workers", "category": "Housing",
        "max_income": 300000, "official_url": "https://mohua.gov.in",
        "description": "Direct benefit transfer vouchers to subsidize monthly rent for industrial migrant workers."
    },
    {
        "id": 84, "name": "Backward Region Grant Fund Housing Project", "category": "Housing",
        "max_income": 250000, "official_url": "https://panchayat.gov.in",
        "description": "Critical infrastructure and housing development grants for backward districts."
    },
    {
        "id": 85, "name": "PM-CARES Children's Housing and Education Fund", "category": "Housing",
        "max_income": 1000000, "official_url": "https://pmcares.gov.in",
        "description": "Corpus fund support providing housing and financial security for children who lost parents during pandemics."
    },
    {
        "id": 86, "name": "Nomadic Tribes Shelter Assistance Scheme", "category": "Housing",
        "max_income": 200000, "official_url": "https://socialjustice.gov.in",
        "description": "Transitional housing and permanent settlement grants for nomadic and semi-nomadic tribes."
    },
    {
        "id": 87, "name": "Smart Cities Mission Slum Integration Housing", "category": "Housing",
        "max_income": 500000, "official_url": "https://smartcities.gov.in",
        "description": "Modern apartment complexes constructed within smart city limits for urban poor households."
    },
    {
        "id": 88, "name": "AMRUT Urban Basic Infrastructure & Housing Link", "category": "Housing",
        "max_income": 700000, "official_url": "https://amrut.gov.in",
        "description": "Assistance ensuring basic civic amenities for newly established housing zones."
    },
    {
        "id": 89, "name": "National Trust Residential Care and Housing Scheme", "category": "Housing",
        "max_income": 400000, "official_url": "https://thenationaltrust.gov.in",
        "description": "Group homes and residential care shelter support for adults with autism, cerebral palsy, and mental retardation."
    },
    {
        "id": 90, "name": "PVTG Special Housing Habitat Development", "category": "Housing",
        "max_income": 200000, "official_url": "https://tribal.nic.in",
        "description": "Dedicated housing packages tailored for Particularly Vulnerable Tribal Groups (PVTGs)."
    },
    {
        "id": 91, "name": "BRICS Green Affordable Housing Initiative", "category": "Housing",
        "max_income": 800000, "official_url": "https://mohua.gov.in",
        "description": "Energy-efficient and low-carbon emission housing construction technology transfer grant."
    },
    {
        "id": 92, "name": "Cooperative Housing Society Promotion Loan Scheme", "category": "Housing",
        "max_income": 1000000, "official_url": "https://ncui.coop",
        "description": "Low-interest financial assistance to registered housing cooperatives for building apartments."
    },
    {
        "id": 93, "name": "Astha Special Housing Scheme for Destitute Women", "category": "Housing",
        "max_income": 180000, "official_url": "https://wcd.nic.in",
        "description": "Short-stay and permanent shelter homes with vocational training for destitute women."
    },
    {
        "id": 94, "name": "Pradhan Mantri Gramin Awas Monitoring & Technology Grant", "category": "Housing",
        "max_income": 500000, "official_url": "https://pmayg.nic.in",
        "description": " geotagging and transparent installment release mechanism for rural home builders."
    },
    {
        "id": 95, "name": "State Police Housing Corporation Low-Cost Loan", "category": "Housing",
        "max_income": 800000, "official_url": "https://www.myscheme.gov.in",
        "description": "Subsidized home construction loans for lower-cadre police personnel and constables."
    },
    {
        "id": 96, "name": "Railway Employee Staff Quarters Upgradation Scheme", "category": "Housing",
        "max_income": 900000, "official_url": "https://indianrailways.gov.in",
        "description": "Modernization and structural safety renovation grants for railway staff residential colonies."
    },
    {
        "id": 97, "name": "Defense Civilian Housing Subsidy Scheme", "category": "Housing",
        "max_income": 700000, "official_url": "https://mod.gov.in",
        "description": "Housing welfare grants for civilian defense establishment workers."
    },
    {
        "id": 98, "name": "Port Trust Workers Affordable Housing Scheme", "category": "Housing",
        "max_income": 600000, "official_url": "https://shipmin.gov.in",
        "description": "Housing development support near major shipping ports for dock and harbor workers."
    },
    {
        "id": 99, "name": "National Sanitation Workers Housing and Welfare Grant", "category": "Housing",
        "max_income": 300000, "official_url": "https://socialjustice.gov.in",
        "description": "Comprehensive housing and health security scheme for municipal sanitation workers."
    },
    {
        "id": 100, "name": "Pradhan Mantri Urban Poor Shelter Renovation Fund", "category": "Housing",
        "max_income": 250000, "official_url": "https://mohua.gov.in",
        "description": "Emergency repair grants for leaking roofs and damaged walls of urban poor dwellings."
    },

    # --- BUSINESS & MSME SCHEMES (101 to 150) ---
    {
        "id": 101, "name": "PM Mudra Yojana (PMMY) - Shishu, Kishor, Tarun", "category": "Business",
        "max_income": 1500000, "official_url": "https://www.mudra.org.in",
        "description": "Collateral-free institutional loans up to ₹10 Lakhs for micro-entrepreneurs and small business owners."
    },
    {
        "id": 102, "name": "PM Vishwakarma Yojana", "category": "Business",
        "max_income": 500000, "official_url": "https://pmvishwakarma.gov.in",
        "description": "End-to-end support including toolkits, skill training, and collateral-free credit up to ₹3 Lakhs for traditional artisans."
    },
    {
        "id": 103, "name": "Stand-Up India Scheme for SC/ST and Women Entrepreneurs", "category": "Business",
        "max_income": 2000000, "official_url": "https://www.standupmitra.in",
        "description": "Bank loans between ₹10 Lakhs and ₹1 Crore for greenfield enterprises in manufacturing, services, or trading."
    },
    {
        "id": 104, "name": "Credit Guarantee Fund Trust for Micro and Small Enterprises (CGTMSE)", "category": "Business",
        "max_income": 2500000, "official_url": "https://www.cgtmse.in",
        "description": "Collateral-free credit guarantee coverage for micro and small industrial units."
    },
    {
        "id": 105, "name": "Prime Minister's Employment Generation Programme (PMEGP)", "category": "Business",
        "max_income": 1000000, "official_url": "https://www.kviconline.gov.in",
        "description": "Credit-linked subsidy scheme for setting up new micro-enterprises in the non-farm sector."
    },
    {
        "id": 106, "name": "Startup India Seed Fund Scheme (SISFS)", "category": "Business",
        "max_income": 5000000, "official_url": "https://www.startupindia.gov.in",
        "description": "Financial assistance to startups for proof of concept, prototype development, and market entry."
    },
    {
        "id": 107, "name": "National Handicraft Development Programme", "category": "Business",
        "max_income": 300000, "official_url": "https://handicrafts.nic.in",
        "description": "Comprehensive welfare, financial credit, and market exposure support for traditional craftspeople."
    },
    {
        "id": 108, "name": "ASPIRE Scheme for Promotion of Innovation in Agro-Rural Industries", "category": "Business",
        "max_income": 1500000, "official_url": "https://msme.gov.in",
        "description": "Setting up livelihood business incubators and technology business incubators in rural agro-sectors."
    },
    {
        "id": 109, "name": "SFURTI Scheme for Traditional Industries Clustering", "category": "Business",
        "max_income": 1000000, "official_url": "https://sfurti.msme.gov.in",
        "description": "Organizing traditional industries and artisans into clusters to make them competitive and sustainable."
    },
    {
        "id": 110, "name": "MSME Market Development Assistance (MDA) Scheme", "category": "Business",
        "max_income": 2000000, "official_url": "https://msme.gov.in",
        "description": "Financial support for micro and small enterprises to participate in international trade fairs and exhibitions."
    },
    {
        "id": 111, "name": "Zero Defect Zero Effect (ZED) Certification Scheme", "category": "Business",
        "max_income": 3000000, "official_url": "https://zed.msme.gov.in",
        "description": "Subsidies and financial assistance for MSMEs to adopt quality standards and eco-friendly manufacturing."
    },
    {
        "id": 112, "name": "RAMP (Raising and Accelerating MSME Performance) Program", "category": "Business",
        "max_income": 4000000, "official_url": "https://ramp.msme.gov.in",
        "description": "World Bank-assisted program improving market access, technology upgradation, and liquidity for MSMEs."
    },
    {
        "id": 113, "name": "National SC/ST Hub Scheme", "category": "Business",
        "max_income": 2000000, "official_url": "https://scsthub.in",
        "description": "Professional support, subsidy, and tender participation assistance for SC/ST entrepreneurs."
    },
    {
        "id": 114, "name": "Procurement and Marketing Support (PMS) Scheme", "category": "Business",
        "max_income": 1500000, "official_url": "https://msme.gov.in",
        "description": "Enhancing marketability of products and services offered by micro and small enterprises."
    },
    {
        "id": 115, "name": "MSME Competitive Lean Manufacturing Scheme", "category": "Business",
        "max_income": 2500000, "official_url": "https://msme.gov.in",
        "description": "Assistance for manufacturing units to reduce wastage, increase productivity, and adopt lean techniques."
    },
    {
        "id": 116, "name": "Design Expertise to Manufacturing MSME Scheme", "category": "Business",
        "max_income": 2000000, "official_url": "https://msme.gov.in",
        "description": "Providing design consultancy support to help MSMEs develop new competitive product designs."
    },
    {
        "id": 117, "name": "Intellectual Property Rights (IPR) Protection for MSME", "category": "Business",
        "max_income": 3000000, "official_url": "https://msme.gov.in",
        "description": "Financial subsidies for patent registration, geographical indications, and trademark filings."
    },
    {
        "id": 118, "name": "Digital MSME Cloud Computing Scheme", "category": "Business",
        "max_income": 1500000, "official_url": "https://msme.gov.in",
        "description": "Encouraging small businesses to adopt cloud computing and enterprise resource planning software."
    },
    {
        "id": 119, "name": "Prime Minister Employment Link Incentive Scheme", "category": "Business",
        "max_income": 5000000, "official_url": "https://labour.gov.in",
        "description": "Incentives to business employers for generating formal new employment and payroll additions."
    },
    {
        "id": 120, "name": "Coir Udyami Yojana for Coir Industry Enterprises", "category": "Business",
        "max_income": 1000000, "official_url": "https://coirboard.gov.in",
        "description": "Credit-linked subsidy scheme for setting up coir fiber and yarn processing industrial units."
    },
    {
        "id": 121, "name": "Mahila Coir Yojana for Women Artisans", "category": "Business",
        "max_income": 300000, "official_url": "https://coirboard.gov.in",
        "description": "Providing motorized spinning rats and financial grants to rural women for coir manufacturing."
    },
    {
        "id": 122, "name": "National Small Industries Corporation (NSIC) Raw Material Assistance", "category": "Business",
        "max_income": 2000000, "official_url": "https://www.nsic.co.in",
        "description": "Financial assistance to MSMEs for procuring raw materials against bank guarantees."
    },
    {
        "id": 123, "name": "NSIC Bill Discounting and Factoring Scheme", "category": "Business",
        "max_income": 2500000, "official_url": "https://www.nsic.co.in",
        "description": "Immediate liquidity support against delayed payments and trade bills for small vendors."
    },
    {
        "id": 124, "name": "SIDBI Make in India Soft Loan Fund for Micro Enterprises (SMILE)", "category": "Business",
        "max_income": 1500000, "official_url": "https://www.sidbi.in",
        "description": "Soft loans with low interest rates to meet debt-equity requirements of new manufacturing units."
    },
    {
        "id": 125, "name": "SIDBI Growth Capital and Venture Assistance Scheme", "category": "Business",
        "max_income": 5000000, "official_url": "https://www.sidbi.in",
        "description": "Equity and quasi-equity investment support for rapidly expanding small businesses."
    },
    {
        "id": 126, "name": "NABARD Rural Business Incubation Fund", "category": "Business",
        "max_income": 1000000, "official_url": "https://www.nabard.org",
        "description": "Grant support for rural start-ups and agri-business innovators."
    },
    {
        "id": 127, "name": "Pradhan Mantri Van Dhan Vikas Yojana (PMVDVY)", "category": "Business",
        "max_income": 300000, "official_url": "https://trifed.tribal.gov.in",
        "description": "Value addition, branding, and packaging units for minor forest produce gathered by tribal entrepreneurs."
    },
    {
        "id": 128, "name": "TRIFED Tribes India Retail Market Access Grant", "category": "Business",
        "max_income": 400000, "official_url": "https://trifed.tribal.gov.in",
        "description": "Global marketing platform and exhibition sponsorship for tribal artisan businesses."
    },
    {
        "id": 129, "name": "National backward Classes Finance & Development Corporation Loan", "category": "Business",
        "max_income": 300000, "official_url": "https://nbcfdc.gov.in",
        "description": "Concessional financial assistance for income-generating business ventures for backward classes."
    },
    {
        "id": 130, "name": "National Scheduled Castes Finance and Development Corporation Scheme", "category": "Business",
        "max_income": 300000, "official_url": "https://nsfdc.nic.in",
        "description": "Term loans and micro-credit for commercial transport, agriculture, and small business setup."
    },
    {
        "id": 131, "name": "National Safai Karamchari Finance & Development Corporation Scheme", "category": "Business",
        "max_income": 300000, "official_url": "https://nskfdc.nic.in",
        "description": "Alternative livelihood financial assistance and business loans for sanitation workers."
    },
    {
        "id": 132, "name": "National Handicapped Finance and Development Corporation Loan", "category": "Business",
        "max_income": 500000, "official_url": "https://nhfdc.nic.in",
        "description": "Concessional loans for self-employment and business ventures for persons with disabilities."
    },
    {
        "id": 133, "name": "North Eastern Regional Agricultural Marketing Corporation Business Grant", "category": "Business",
        "max_income": 800000, "official_url": "https://neramac.com",
        "description": "Commercial promotion and processing unit setup assistance for businesses in the North-East."
    },
    {
        "id": 134, "name": "Food Processing Industries Cold Chain and Value Addition Infrastructure", "category": "Business",
        "max_income": 3000000, "official_url": "https://mofpi.gov.in",
        "description": "Capital subsidies for setting up cold storage, refrigerated vans, and food processing plant units."
    },
    {
        "id": 135, "name": "PM Formalisation of Micro Food Processing Enterprises (PMFME) Scheme", "category": "Business",
        "max_income": 1000000, "official_url": "https://pmfme.mofpi.gov.in",
        "description": "Credit-linked subsidy of 35% (up to ₹10 Lakhs) for upgrading micro food processing units."
    },
    {
        "id": 136, "name": "Pradhan Mantri Kisan Sampada Yojana Enterprise Grant", "category": "Business",
        "max_income": 4000000, "official_url": "https://mofpi.gov.in",
        "description": "Modern infrastructure creation from farm gate to retail outlet for agro-enterprises."
    },
    {
        "id": 137, "name": "National Fisheries Development Board (NFDB) Business Venture Grant", "category": "Business",
        "max_income": 1500000, "official_url": "https://nfdb.gov.in",
        "description": "Financial assistance for fish seed hatcheries, feed mills, and commercial fish processing units."
    },
    {
        "id": 138, "name": "Animal Husbandry Infrastructure Development Fund (AHIDF)", "category": "Business",
        "max_income": 5000000, "official_url": "https://ahidf.udyamimitra.in",
        "description": "Interest subvention for establishing dairy processing, meat processing, and animal feed plants."
    },
    {
        "id": 139, "name": "National Bamboo Mission Enterprise Development Grant", "category": "Business",
        "max_income": 1000000, "official_url": "https://nbm.nic.in",
        "description": "Support for bamboo-based handicraft, furniture, and industrial charcoal manufacturing units."
    },
    {
        "id": 140, "name": "Export Promotion Council for Handicrafts Startup Support", "category": "Business",
        "max_income": 2000000, "official_url": "https://www.epch.in",
        "description": "Assistance for handicraft exporters to enter international markets and showcase goods globally."
    },
    {
        "id": 141, "name": "Leather Sector Skill Development and Business Grant", "category": "Business",
        "max_income": 1500000, "official_url": "https://leatherindia.org",
        "description": "Modernization subsidies for leather footwear and garment manufacturing micro-enterprises."
    },
    {
        "id": 142, "name": "Textile Cluster Development and Powerloom Modernization Scheme", "category": "Business",
        "max_income": 2000000, "official_url": "https://texmin.nic.in",
        "description": "Technology upgradation fund and capital subsidy for powerloom and textile weaving businesses."
    },
    {
        "id": 143, "name": "Jute Mark India Quality Certification Business Scheme", "category": "Business",
        "max_income": 1000000, "official_url": "https://jute.gov.in",
        "description": "Promoting authentic jute diversified products and offering marketing subsidies to jute entrepreneurs."
    },
    {
        "id": 144, "name": "GeM (Government e-Marketplace) Vendor Registration Support", "category": "Business",
        "max_income": 5000000, "official_url": "https://gem.gov.in",
        "description": "Training and onboarding assistance for micro and small enterprises to sell goods directly to government departments."
    },
    {
        "id": 145, "name": "Credit Guarantee Scheme for Startups (CGSS)", "category": "Business",
        "max_income": 5000000, "official_url": "https://www.startupindia.gov.in",
        "description": "Providing credit guarantees to financial institutions for loans extended to eligible DPIIT-recognized startups."
    },
    {
        "id": 146, "name": "MeitY TIDE 2.0 Startup Incubation Scheme", "category": "Business",
        "max_income": 5000000, "official_url": "https://meity.gov.in",
        "description": "Financial grants and incubation support for tech startups using emerging technologies like AI, IoT, and Robotics."
    },
    {
        "id": 147, "name": "NIDHI PRAYAS Grant for Technology Innovators", "category": "Business",
        "max_income": 3000000, "official_url": "https://dst.gov.in",
        "description": "Translating innovative ideas and technological prototypes into commercial startup ventures."
    },
    {
        "id": 148, "name": " BIRAC BIG (Biotechnology Ignition Grant)", "category": "Business",
        "max_income": 5000000, "official_url": "https://birac.nic.in",
        "description": "Seed funding of up to ₹50 Lakhs for biotech entrepreneurs and healthcare startups."
    },
    {
        "id": 149, "name": "Software Technology Parks of India (STPI) Export Incubation", "category": "Business",
        "max_income": 5000000, "official_url": "https://www.stpi.in",
        "description": "Plug-and-play workspace infrastructure and high-speed data communication support for IT/ITeS startups."
    },
    {
        "id": 150, "name": "National Small Business Digital Transformation Grant", "category": "Business",
        "max_income": 2000000, "official_url": "https://msme.gov.in",
        "description": "Subsidies for small businesses adopting e-commerce websites and digital payment gateways."
    },

    # --- AGRICULTURE SCHEMES (151 to 200) ---
    {
        "id": 151, "name": "PM-KISAN (Pradhan Mantri Kisan Samman Nidhi)", "category": "Agriculture",
        "max_income": 500000, "official_url": "https://pmkisan.gov.in",
        "description": "Direct income support of ₹6,000 per year in three equal installments to all landholding farmer families."
    },
    {
        "id": 152, "name": "Pradhan Mantri Fasal Bima Yojana (PMFBY)", "category": "Agriculture",
        "max_income": 600000, "official_url": "https://pmfby.gov.in",
        "description": "Comprehensive crop insurance scheme protecting farmers against natural calamities at minimal premium rates."
    },
    {
        "id": 153, "name": "Kisan Credit Card (KCC) Scheme", "category": "Agriculture",
        "max_income": 500000, "official_url": "https://www.nabard.org",
        "description": "Timely and adequate credit support with subsidized interest rates for farmers' cultivation and operational needs."
    },
    {
        "id": 154, "name": "Agriculture Infrastructure Fund (AIF)", "category": "Agriculture",
        "max_income": 1000000, "official_url": "https://agriinfra.dac.gov.in",
        "description": "Medium-long term debt financing facility for investment in post-harvest management infrastructure and community farming assets."
    },
    {
        "id": 155, "name": "PM Krishi Sinchayee Yojana (PMKSY) - Per Drop More Crop", "category": "Agriculture",
        "max_income": 400000, "official_url": "https://pmksy.gov.in",
        "description": "Subsidies for drip and sprinkler micro-irrigation systems to enhance water-use efficiency in farming."
    },
    {
        "id": 156, "name": "National Mission on Sustainable Agriculture (NMSA)", "category": "Agriculture",
        "max_income": 500000, "official_url": "https://nmsa.dac.gov.in",
        "description": "Promoting organic farming, soil health card management, and climate-resilient agricultural practices."
    },
    {
        "id": 157, "name": "Sub-Mission on Agricultural Mechanization (SMAM)", "category": "Agriculture",
        "max_income": 400000, "official_url": "https://agrimachinery.nic.in",
        "description": "Financial subsidies up to 50%-80% for purchasing tractors, power tillers, and modern agricultural equipment."
    },
    {
        "id": 158, "name": "Paramparagat Krishi Vikas Yojana (PKVY)", "category": "Agriculture",
        "max_income": 500000, "official_url": "https://pgsindia-ncof.gov.in",
        "description": "Promoting commercial organic farming clusters and chemical-free agricultural produce certification."
    },
    {
        "id": 159, "name": "National Bamboo Mission Agroforestry Scheme", "category": "Agriculture",
        "max_income": 600000, "official_url": "https://nbm.nic.in",
        "description": "Encouraging farmers to cultivate bamboo on farm boundaries and wasteland patches for extra income."
    },
    {
        "id": 160, "name": "National Beekeeping and Honey Mission (NBHM)", "category": "Agriculture",
        "max_income": 500000, "official_url": "https://nbhm.gov.in",
        "description": "Promoting scientific honey bee keeping and honey production as an allied farming activity."
    },
    {
        "id": 161, "name": "National Livestock Mission (NLM) Entrepreneurship Grant", "category": "Agriculture",
        "max_income": 800000, "official_url": "https://nlm.udyamimitra.in",
        "description": "Capital subsidies for poultry, sheep, goat, and piggery breeding farm establishment."
    },
    {
        "id": 162, "name": "Rashtriya Krishi Vikas Yojana (RKVY) Agri-Preneurship", "category": "Agriculture",
        "max_income": 1000000, "official_url": "https://rkvy.nic.in",
        "description": "Strengthening infrastructure in agriculture and allied sectors with startup grants for agri-graduates."
    },
    {
        "id": 163, "name": "Pradhan Mantri Matsya Sampada Yojana (PMMSY)", "category": "Agriculture",
        "max_income": 800000, "official_url": "https://dof.gov.in",
        "description": "Comprehensive development of marine and inland fisheries, aquaculture ponds, and fishing boat subsidies."
    },
    {
        "id": 164, "name": "National Horticulture Mission (MIDH)", "category": "Agriculture",
        "max_income": 600000, "official_url": "https://midh.gov.in",
        "description": "Subsidies for horticulture crop cultivation, protected greenhouse farming, and nurseries."
    },
    {
        "id": 165, "name": "Soil Health Card Scheme and Nutrient Support", "category": "Agriculture",
        "max_income": 400000, "official_url": "https://soilhealth.dac.gov.in",
        "description": "Testing soil nutrient status and providing customized fertilizer dosage recommendations to farmers."
    },
    {
        "id": 166, "name": "National e-Governance Plan in Agriculture (NeGP-A)", "category": "Agriculture",
        "max_income": 1000000, "official_url": "https://agricoop.nic.in",
        "description": "Digital farmer portals, weather advisory apps, and electronic marketplace integration (e-NAM)."
    },
    {
        "id": 167, "name": "e-NAM (National Agriculture Market) Trading Portal Subsidy", "category": "Agriculture",
        "max_income": 1000000, "official_url": "https://www.enam.gov.in",
        "description": "Unified online wholesale agricultural produce trading portal connecting APMC mandis across India."
    },
    {
        "id": 168, "name": "Sub-Mission on Seed and Planting Material (SMSP)", "category": "Agriculture",
        "max_income": 500000, "official_url": "https://seednet.gov.in",
        "description": "Providing certified high-yielding quality seeds and seed production training to farmers."
    },
    {
        "id": 169, "name": "National Mission on Edible Oils - Oilseeds (NMEO-OS)", "category": "Agriculture",
        "max_income": 600000, "official_url": "https://nmeo.dac.gov.in",
        "description": "Financial incentives and planting material assistance for domestic oilseed crop production."
    },
    {
        "id": 170, "name": "National Mission on Edible Oils - Oil Palm (NMEO-OP)", "category": "Agriculture",
        "max_income": 800000, "official_url": "https://nmeo.dac.gov.in",
        "description": "Special assistance, planting grants, and price protection for oil palm plantation farmers."
    },
    {
        "id": 171, "name": "Sub-Mission on Agro-Forestry (SMAF)", "category": "Agriculture",
        "max_income": 500000, "official_url": "https://nmsa.dac.gov.in",
        "description": "Encouraging tree plantation on farm lands ('Har Medh Par Ped') for timber and carbon credits."
    },
    {
        "id": 172, "name": "Dairy Processing and Infrastructure Development Fund (DIDF)", "category": "Agriculture",
        "max_income": 1500000, "official_url": "https://www.nddb.org",
        "description": "Modernization of milk chilling, processing plants, and value-added product manufacturing units."
    },
    {
        "id": 173, "name": "National Dairy Plan Phase II Support", "category": "Agriculture",
        "max_income": 800000, "official_url": "https://www.nddb.org",
        "description": "Increasing productivity of milch animals and providing better market access for dairy farmers."
    },
    {
        "id": 174, "name": "Poultry Venture Capital Fund Subsidy", "category": "Agriculture",
        "max_income": 600000, "official_url": "https://dahd.nic.in",
        "description": "Financial assistance for setting up commercial broiler and layer poultry farming units."
    },
    {
        "id": 175, "name": "Foot and Mouth Disease Control Programme (FMD-CP)", "category": "Agriculture",
        "max_income": 1000000, "official_url": "https://dahd.nic.in",
        "description": "Free vaccination and health security coverage for cattle, buffalo, sheep, goats, and pigs."
    },
    {
        "id": 176, "name": "National Animal Disease Control Programme (NADCP)", "category": "Agriculture",
        "max_income": 1000000, "official_url": "https://dahd.nic.in",
        "description": "Eradication of livestock diseases through mass tagging, diagnostics, and vaccination."
    },
    {
        "id": 177, "name": "Kisan Urja Suraksha evam Utthaan Mahabhiyan (PM-KUSUM Component A)", "category": "Agriculture",
        "max_income": 1000000, "official_url": "https://pmkusum.mnre.gov.in",
        "description": "Setting up 10,000 MW of decentralized solar power plants on barren or agricultural lands for extra income."
    },
    {
        "id": 178, "name": "PM-KUSUM Component B (Solar Water Pumps)", "category": "Agriculture",
        "max_income": 600000, "official_url": "https://pmkusum.mnre.gov.in",
        "description": "Installation of standalone off-grid solar agriculture water pumps with 60%-90% government subsidy."
    },
    {
        "id": 179, "name": "PM-KUSUM Component C (Solarization of Grid Pumps)", "category": "Agriculture",
        "max_income": 800000, "official_url": "https://pmkusum.mnre.gov.in",
        "description": "Solarization of existing grid-connected agriculture pumps to provide reliable daytime solar irrigation."
    },
    {
        "id": 180, "name": "Farmer Producer Organization (FPO) Formation and Promotion Scheme", "category": "Agriculture",
        "max_income": 1000000, "official_url": "https://sfacindia.com",
        "description": "Financial grant of up to ₹15 Lakhs per FPO to aggregate small farmers and boost bargaining power."
    },
    {
        "id": 181, "name": "NABARD Producer Organization Development Fund (PODF)", "category": "Agriculture",
        "max_income": 1500000, "official_url": "https://www.nabard.org",
        "description": "Credit and grant support for capacity building and working capital of farmer producer companies."
    },
    {
        "id": 182, "name": "National Cooperative Development Corporation (NCDC) Agri-Loan", "category": "Agriculture",
        "max_income": 2000000, "official_url": "https://www.ncdc.in",
        "description": "Financial assistance to agricultural cooperatives for processing, storage, and marketing infrastructure."
    },
    {
        "id": 183, "name": "Mission Organic Value Chain Development for North Eastern Region", "category": "Agriculture",
        "max_income": 600000, "official_url": "https://movcdner.gov.in",
        "description": "End-to-end organic value chain development from seeds to export markets in North-Eastern states."
    },
    {
        "id": 184, "name": "Central Sector Scheme for Promotion of Agricultural Extension", "category": "Agriculture",
        "max_income": 500000, "official_url": "https://agricoop.nic.in",
        "description": "Agri-clinics and agri-business centres (ACABC) scheme providing training and credit to agricultural graduates."
    },
    {
        "id": 185, "name": "National Institute of Agricultural Extension Management (MANAGE) Grant", "category": "Agriculture",
        "max_income": 800000, "official_url": "https://www.manage.gov.in",
        "description": "Training extension officers and supporting rural agri-entrepreneurs with modern techniques."
    },
    {
        "id": 186, "name": "Krishi Vigyan Kendra (KVK) Technology Demonstration Grant", "category": "Agriculture",
        "max_income": 600000, "official_url": "https://icar.org.in",
        "description": "On-farm testing and frontline demonstrations of latest agricultural technologies for farmers."
    },
    {
        "id": 187, "name": "ICAR Farmer FIRST Programme", "category": "Agriculture",
        "max_income": 500000, "official_url": "https://icar.org.in",
        "description": "Connecting agricultural scientists directly with farmers for integrated farming system demonstrations."
    },
    {
        "id": 188, "name": "Attracting and Retaining Youth in Agriculture (ARYA) Scheme", "category": "Agriculture",
        "max_income": 500000, "official_url": "https://icar.org.in",
        "description": "Involving rural youth in profitable agricultural enterprises like mushroom cultivation, honey, and seed processing."
    },
    {
        "id": 189, "name": "National Innovation on Climate Resilient Agriculture (NICRA)", "category": "Agriculture",
        "max_income": 600000, "official_url": "https://nicra.icar.gov.in",
        "description": "Research and demonstration of climate-resilient crop varieties and water conservation techniques."
    },
    {
        "id": 190, "name": "Sub-Mission on Agricultural Plant Protection and Quarantine", "category": "Agriculture",
        "max_income": 400000, "official_url": "https://ppqs.gov.in",
        "description": "Pest surveillance, drone-based pesticide application subsidies, and biopesticide promotion."
    },
    {
        "id": 191, "name": "National Bee Board Honey Testing Laboratory Grant", "category": "Agriculture",
        "max_income": 1000000, "official_url": "https://nbhm.gov.in",
        "description": "Subsidies for establishing honey testing laboratories and quality standardization centers."
    },
    {
        "id": 192, "name": "Pradhan Mantri Matsya Kisan Samridhi Sah-Yojana (PM-MKSSY)", "category": "Agriculture",
        "max_income": 800000, "official_url": "https://dof.gov.in",
        "description": "Formalizing fisheries sector, micro-enterprise growth, and performance grants for aqua farmers."
    },
    {
        "id": 193, "name": "National Inland Fisheries Infrastructure Development Fund", "category": "Agriculture",
        "max_income": 1000000, "official_url": "https://dof.gov.in",
        "description": "Subsidies for developing reservoirs, river basins, and freshwater fish landing centers."
    },
    {
        "id": 194, "name": "Marine Fisheries Motorization and Safety Scheme", "category": "Agriculture",
        "max_income": 400000, "official_url": "https://dof.gov.in",
        "description": "Subsidies for installing outboard motors on traditional fishing boats and safety communication gear."
    },
    {
        "id": 195, "name": "State Agricultural Produce Market Committee (APMC) Modernization Grant", "category": "Agriculture",
        "max_income": 1000000, "official_url": "https://www.myscheme.gov.in",
        "description": "Upgrading rural wholesale markets with electronic weighing scales, grading floors, and cold rooms."
    },
    {
        "id": 196, "name": "National Agricultural Disaster Relief and Crop Compensation Fund", "category": "Agriculture",
        "max_income": 500000, "official_url": "https://agricoop.nic.in",
        "description": "Immediate input subsidy disbursement for farmers suffering crop loss due to unseasonal rains, drought, or floods."
    },
    {
        "id": 197, "name": "NABARD Micro-Irrigation Fund (MIF)", "category": "Agriculture",
        "max_income": 800000, "official_url": "https://www.nabard.org",
        "description": "Dedicated fund for state governments and farmers to expand micro-irrigation network coverage."
    },
    {
        "id": 198, "name": "Pradhan Mantri Kisan Maan-Dhyan Yojana (PM-SYM / PM-KMY)", "category": "Agriculture",
        "max_income": 200000, "official_url": "https://maandhan.in",
        "description": "Old age pension security scheme providing ₹3,000 monthly pension for small and marginal farmers after age 60."
    },
    {
        "id": 199, "name": "National Watershed Development Project for Rainfed Areas", "category": "Agriculture",
        "max_income": 400000, "official_url": "https://dolr.gov.in",
        "description": "Harnessing rainwater runoff, soil conservation, and biomass generation in rainfed farming zones."
    },
    {
        "id": 200, "name": "Pradhan Mantri Krishi Vikas and Rural Livelihood Integration Grant", "category": "Agriculture",
        "max_income": 500000, "official_url": "https://rural.nic.in",
        "description": "Integrated rural livelihood support combining farming assistance with self-help group micro-credit."
    }
]

# ==================== API ENDPOINTS ====================

@app.get("/api/health")
def health_check():
    return {"status": "online", "total_schemes_loaded": len(ALL_SCHEMES)}

@app.post("/api/recommendations/evaluate")
def evaluate_eligibility(profile: UserProfile):
    eligible = []
    
    for scheme in ALL_SCHEMES:
        # Check income threshold
        if profile.income <= scheme["max_income"]:
            # Additional contextual matching logic can be added here
            eligible.append(scheme)
            
    return {
        "total_evaluated": len(ALL_SCHEMES),
        "eligible_count": len(eligible),
        "eligible_schemes": eligible
    }

@app.get("/api/schemes", response_model=List[dict])
def get_all_schemes():
    return ALL_SCHEMES

@app.post("/api/chat")
def chat_assistant(payload: ChatMessage):
    query = payload.message.lower()
    
    if "document" in query or "aadhaar" in query or "papers" in query:
        response = "Generally, you need an Aadhaar card, Income Certificate, Passport-size photo, Residence Proof, and a Bank Account passbook linked with Aadhaar."
    elif "income" in query:
        response = "Income limits vary by scheme. Most welfare schemes require annual family income to be below ₹3 Lakhs to ₹8 Lakhs."
    elif "loan" in query:
        response = "There are several loan schemes like PM Mudra Yojana (up to ₹10 Lakhs) and Stand-Up India (up to ₹1 Crore) for businesses."
    else:
        response = f"I have analyzed your query about '{payload.message}'. SchemeAI has loaded 200 national schemes across Education, Housing, Business, and Agriculture. Use the Finder tab to check your eligibility!"
        
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)