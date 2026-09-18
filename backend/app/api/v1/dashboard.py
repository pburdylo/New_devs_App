from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, List, Any
from app.services.cache import get_revenue_summary
from app.core.auth import authenticate_request as get_current_user

router = APIRouter()

@router.get("/dashboard/summary")
async def get_dashboard_summary(
    property_id: str,
    current_user: dict = Depends(get_current_user)
) -> Dict[str, Any]:
    
    tenant_id = getattr(current_user, "tenant_id", "default_tenant") or "default_tenant"
    
    revenue_data = await get_revenue_summary(property_id, tenant_id)
    
    total_revenue_float = float(revenue_data['total'])
    
    return {
        "property_id": revenue_data['property_id'],
        "total_revenue": total_revenue_float,
        "currency": revenue_data['currency'],
        "reservations_count": revenue_data['count']
    }

@router.get("/dashboard/properties")
async def get_dashboard_properties(
    current_user: dict = Depends(get_current_user)
) -> List[Dict[str, Any]]:

    tenant_id = getattr(current_user, "tenant_id", "default_tenant") or "default_tenant"
    
    properties = [
        {"id": "prop-001", "name": "Beach House Alpha"},
        {"id": "prop-002", "name": "City Apartment Downtown"},
        {"id": "prop-003", "name": "Country Villa Estate"},
        {"id": "prop-004", "name": "Lakeside Cottage"},
        {"id": "prop-005", "name": "Urban Loft Modern"},
    ]

    return properties