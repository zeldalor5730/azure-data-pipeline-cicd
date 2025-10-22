provider "azurerm" { features {} }

resource "azurerm_resource_group" "rg" {
  name     = "rg-dataeng-prod"
  location = "East US"
}

resource "azurerm_storage_account" "data_storage" {
  name                     = "datastorageprod"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}
