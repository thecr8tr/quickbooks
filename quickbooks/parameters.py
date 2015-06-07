from xml.etree import ElementTree as ET

__author__ = 'thecr8tr'

class empty_class():
    def __init__(self):
        pass

class search_parameter():
    def __init__(self):
        pass

    def set_attributes(self):

        # how to proceed once qbxml encounters an error
        self.onError = 'stopOnError' #options = stopOnError, continueOnError

        # returns a count of items to be returned
        self.metaData = 'NoMetaData' #options = NoMetaData, MetaDataOnly, MetaDataAndResponseData

        # sets request as an iterator/use Max Return to control how many items are sent at a time
        self.iterator = None #options = Start, Continue, Stop

        # returns only items with indicated name
        self.FullName = None #FullName comes from QB File and Must include Parents if applicable

        # returns only items with indicated list id number.
        # Be careful!!!, List ID's are only specific within lists.
        # (An id may be for a name and a transaction)
        self.ListID = None #ListID comes from QB File

        # limits the number of items returned
        self.MaxReturned = None #options = any integer greater than zero as a string

        # filters active status, default is ActiveOnly
        self.ActiveStatus = None #options = ActiveOnly, InactiveOnly, All

        # filters for items on or after specified date
        self.FromModifiedDate = None #options = YYYY+'-'+MM+'-'+DD[+'T'+hh[+':'+mm[+':'+ss[+'-'+hh+':'+mm]]]]

        # filters for items on or before specified date
        self.ToModifiedDate = None #options = YYYY+'-'+MM+'-'+DD[+'T'+hh[+':'+mm[+':'+ss[+'-'+hh+':'+mm]]]]

        # filters for object name
        self.NameFilter = empty_class()

        # NameFilter search parameters
        self.NameFilter.MatchCriterion = None # options = StartsWith, Contains, EndsWith

        # NameFilter search value (can be all or part)
        self.NameFilter.Name = None # user supplied string to match from

        # filters for object name between two user supplied names
        self.NameRangeFilter = empty_class()

        # NameRangeFilter search start value (omit to search from beginning of list)
        self.NameRangeFilter.FromName = None # user supplied string to start match

        # NameRangeFilter search end value (omit to search to end of list)
        self.NameRangeFilter.ToName = None # user supplied string to end match

        # Filters based on the amount of the total balance (includes sub accounts)
        self.TotalBalanceFilter = empty_class()

        # TotalBalanceFilter
        self.TotalBalanceFilter.Operator = None # options = LessThan, LessThanEqual, Equal, GreaterThan,
                                                          # GreaterThanEqual

        # TotalBalanceFilter amount to search for (customers and vendors only)
        self.TotalBalanceFilter.Amount = None # user supplied string of a 2 decimal place dollar amount

        # filters for object name between two user supplied names
        self.CurrencyFilter = empty_class()

        # CurrencyFilter
        self.CurrencyFilter.ListID = None # ListID comes from QB File

        # CurrencyFilter
        self.CurrencyFilter.FullName = None # FullName comes from QB File and Must include Parents if applicable

        # filters for object name between two user supplied names
        self.ClassFilter = empty_class()

        # ClassFilter
        self.ClassFilter.ListID = None # ListID comes from QB File

        # ClassFilter
        self.ClassFilter.FullName = None # FullName comes from QB File and Must include Parents if applicable

        # ClassFilter Returns item w/ ListID and its decendants
        self.ClassFilter.ListIDWithChildren = None # ListID comes from QB File

        # ClassFilter Returns item w/ FullName and its decendants
        self.ClassFilter.FullNameWithChildren = None # FullName comes from QB File and Must include Parents if applicable

        # Allows you to filter data
        self.IncludeRetElement = None # options = xml tags as a list

        # Refers to the owner of a data extension:
        # If OwnerID is 0, this is a public data extension, also known as a custom field. Custom fields appear
                # in the QuickBooks UI.
        # If OwnerID is a GUID, for example {6B063959-81B0-4622-85D6-F548C8CCB517}, this field is a private data
                # extension defined by an integrated application. Private data extensions do not appear in the
                # QuickBooks UI.
        # Note that OwnerID values are not case-sensitive, meaning that if you enter an OwnerID value with lower-case
                # letters, the value will be saved and returned with upper-case letters.
        # When you share a private data extension with another application, the other application must know both the
                # OwnerID and the DataExtName, as these together form a data extension's unique name.
        self.OwnerID = None # options = ????

        # Allows specification of Account type in AccountQueryRq only
        self.AccountType = None # options = Accounts Payable, Accounts Receivable, Bank, Credit Card....

        # Applicable to the ToDoQueryRq returns a done, not done, or both list of elements
        self.DoneStatus = None # options = NotDoneOnly(default), DoneOnly, All

        # filter for a certain transaction id or reference number, TxnID are unique
        self.TxnID = None # QuickBooks set item

        # This is based on a QuickBooks Supplied Date/Time
        self.ModifiedDateRangeFilter = empty_class()

        # This is based on a QuickBooks Supplied Date/Time
        self.ModifiedDateRangeFilter.FromModifiedDate = None #options = YYYY+'-'+MM+'-'+DD[+'T'+hh[+':'+mm[+':'+ss[+'-'+hh+':'+mm]]]]

        # This is based on a QuickBooks Supplied Date/Time
        self.ModifiedDateRangeFilter.ToModifiedDate = None #options = YYYY+'-'+MM+'-'+DD[+'T'+hh[+':'+mm[+':'+ss[+'-'+hh+':'+mm]]]]

        # This is based on the user Supplied Date
        self.TxnDateRangeFilter = empty_class()

        # This is based on a QuickBooks Supplied Date/Time
        self.TxnDateRangeFilter.FromTxnDate = None #options = YYYY+'-'+MM+'-'+DD

        # This is based on a QuickBooks Supplied Date/Time
        self.TxnDateRangeFilter.ToTxnDate = None #options = YYYY+'-'+MM+'-'+DD

        #
        self.DateMacro = None # options ThisWeekToDate, ThisMonthToDate, LastWeek, LastFiscalQuarter, LastFiscalYear...

        # EntityFilter
        self.EntityFilter = empty_class() # options FullName, ListID, FullNameWithChildren, or ListIDWithChildren

        # EntityFilter
        self.EntityFilter.ListID = None # ListID comes from QB File

        # EntityFilter
        self.EntityFilter.FullName = None # FullName comes from QB File and Must include Parents if applicable

        # EntityFilter Returns item w/ ListID and its decendants
        self.EntityFilter.ListIDWithChildren = None # ListID comes from QB File

        # EntityFilter Returns item w/ FullName and its decendants
        self.EntityFilter.FullNameWithChildren = None # FullName comes from QB File and Must include Parents if applicable

        # AccountFilter --- Only works on the main account Associated with trans (ie, bank account for check or deposit)
        self.AccountFilter = empty_class() # options FullName, ListID, FullNameWithChildren, or ListIDWithChildren

        # AccountFilter
        self.AccountFilter.ListID = None # ListID comes from QB File

        # AccountFilter
        self.AccountFilter.FullName = None # FullName comes from QB File and Must include Parents if applicable

        # AccountFilter Returns item w/ ListID and its decendants
        self.AccountFilter.ListIDWithChildren = None # ListID comes from QB File

        # AccountFilter Returns item w/ FullName and its decendants
        self.AccountFilter.FullNameWithChildren = None # FullName comes from QB File and Must include Parents if applicable

        # PaidStatus searches for invoices or bills that have been paid
        self.PaidStatus = None # options = All (default), PaidOnly, NotPaidOnly

        # IncludeLinkedTxns will show transactions that are linked to filtered transactions (ie a check that pays a bill)
        self.IncludeLinkedTxns = None # options = False (default), True

        # IncludeLineItems will show the transaction splits
        self.IncludeLineItems = None # option = False (default), True

        # TransactionQueryRq Specific
        self.TransactionFilter = None # options = specific transaction types or All

        # TransactionQueryRq Specific
        self.TransactionDetailLevelFilter = None # All, SummaryOnly, AllExceptSummary

        # TransactionQueryRq Specific
        self.TransactionPostingStatusFilter = None # Either, NonPosting, Posting

        # TransactionQueryRq Specific
        self.TransactionPaidStatusFilter = None # Either, Closed, Open

        # Insert value to define the case-insensitive name of a new list object
        self.Name = None # XML String type

        # This is a string not a python boolean
        self.RefNumber = None # true, false, 1, 0

        # CustomerAdd.ClassRef
        self.ClassRef = empty_class()

        # According to the docs, this is set automatically by QB when you add the item
        self.ClassRef.ListID = None

        # Use this to designate the hierarchy for the new item
        self.ClassRef.FullName = None

        # CustomerAdd.ClassRef
        self.ParentRef = empty_class()

        # According to the docs, this is set automatically by QB when you add the item
        self.ParentRef.ListID = None

        # Use this to designate the hierarchy for the new item
        self.ParentRef.FullName = None

        #
        self.CompanyName = None #

        #
        self.Salutation = None #

        #
        self.FirstName = None #

        #
        self.MiddleName = None #

        #
        self.LastName = None #

        #
        self.JobTitle = None #

        #
        self.BillAddress = empty_class() #

        #
        self.BillAddress.Addr1 = None #

        #
        self.BillAddress.Addr2 = None #

        #
        self.BillAddress.Addr3 = None #

        #
        self.BillAddress.Addr4 = None #

        #
        self.BillAddress.Addr5 = None #

        #
        self.BillAddress.City = None #

        #
        self.BillAddress.State = None #

        #
        self.BillAddress.PostalCode = None #

        #
        self.BillAddress.Country = None #

        #
        self.BillAddress.Note = None #

        #
        self.ShipAddress = empty_class() #

        #
        self.ShipAddress.Addr1 = None #

        #
        self.ShipAddress.Addr2 = None #

        #
        self.ShipAddress.Addr3 = None #

        #
        self.ShipAddress.Addr4 = None #

        #
        self.ShipAddress.Addr5 = None #

        #
        self.ShipAddress.City = None #

        #
        self.ShipAddress.State = None #

        #
        self.ShipAddress.PostalCode = None #

        #
        self.ShipAddress.Country = None #

        #
        self.ShipAddress.Note = None #

        #
        self.ShipToAddress = empty_class() #

        #
        self.ShipToAddress.Addr1 = None #

        #
        self.ShipToAddress.Addr2 = None #

        #
        self.ShipToAddress.Addr3 = None #

        #
        self.ShipToAddress.Addr4 = None #

        #
        self.ShipToAddress.Addr5 = None #

        #
        self.ShipToAddress.City = None #

        #
        self.ShipToAddress.State = None #

        #
        self.ShipToAddress.PostalCode = None #

        #
        self.ShipToAddress.Country = None #

        #
        self.ShipToAddress.Note = None #

        #
        self.ShipToAddress.DefaultShipTo = None #

        #
        self.Phone = None

        #
        self.AltPhone = None

        #
        self.Fax = None

        #
        self.Email = None

        #
        self.Cc = None

        #
        self.Contact = None

        #
        self.AltContact = None

        #
        self.AdditionalContactRef = empty_class() #

        #
        self.AdditionalContactRef.ContactName = None #

        #
        self.AdditionalContactRef.ContactValue = None #

        #
        self.Contacts = empty_class() #

        #
        self.Contacts.Salutation = None #

        #
        self.Contacts.FirstName = None #

        #
        self.Contacts.MiddleName = None #

        #
        self.Contacts.LastName = None #

        #
        self.Contacts.JobTitle = None #

        #
        self.Contacts.AdditionalContactRef = empty_class() #

        #
        self.Contacts.AdditionalContactRef.ContactName = None #

        #
        self.Contacts.AdditionalContactRef.ContactValue = None #

        #
        self.CustomerTypeRef = empty_class() #

        #
        self.CustomerTypeRef.ListID = None #

        #
        self.CustomerTypeRef.FullName = None #

        #
        self.TermsRef = empty_class() #

        #
        self.TermsRef.ListID = None #

        #
        self.TermsRef.FullName = None #

        #
        self.SalesRepRef = empty_class() #

        #
        self.SalesRepRef.ListID = None #

        #
        self.SalesRepRef.FullName = None #

        #
        self.OpenBalance = None #

        #
        self.OpenBalanceDate = None #

        #
        self.SalesTaxCodeRef = empty_class() #

        #
        self.SalesTaxCodeRef.ListID = None #

        #
        self.SalesTaxCodeRef.FullName = None #

        #
        self.ItemSalesTaxRef = empty_class() #

        #
        self.ItemSalesTaxRef.ListID = None #

        #
        self.ItemSalesTaxRef.FullName = None #

        #
        self.ResaleNumber = None #

        #
        self.AccountNumber = None #

        #
        self.CreditLimit = None #

        #
        self.PreferredPaymentMethodRef = empty_class() #

        #
        self.PreferredPaymentMethodRef.ListID = None #

        #
        self.PreferredPaymentMethodRef.FullName = None #

        #
        self.CreditCardInfo = empty_class() #

        #
        self.CreditCardInfo.CreditCardNumber = None #

        #
        self.CreditCardInfo.ExpirationMonth = None #

        #
        self.CreditCardInfo.ExpirationYear = None #

        #
        self.CreditCardInfo.NameOnCard = None #

        #
        self.CreditCardInfo.CreditCardAddress = None #

        #
        self.CreditCardInfo.CreditCardPostalCode = None #

        #
        self.JobStatus = None #

        #
        self.JobStartDate = None #

        #
        self.JobProjectedEndDate = None #

        #
        self.JobEndDate = None #

        #
        self.JobDesc = None #

        #
        self.JobTypeRef = empty_class() #

        #
        self.JobTypeRef.ListID = None #

        #
        self.JobTypeRef.FullName = None #

        #
        self.Notes = None #

        #
        self.AdditionalNotes = empty_class() #

        #
        self.AdditionalNotes.Notes = None #

        #
        self.PreferredDeliveryMethod = None #

        #
        self.PriceLevelRef = empty_class() #

        #
        self.PriceLevelRef.ListID = None #

        #
        self.PriceLevelRef.FullName = None #

        #
        self.ExternalGUID = None #

        #
        self.CurrencyRef = empty_class() #

        #
        self.CurrencyRef.ListID = None #

        #
        self.CurrencyRef.FullName = None #

        #
        self.AccountRef = empty_class() #

        #
        self.AccountRef.ListID = None #

        #
        self.AccountRef.FullName = None #

        #
        self.PayeeEntityRef = empty_class() #

        #
        self.PayeeEntityRef.ListID = None #

        #
        self.PayeeEntityRef.FullName = None #

        #
        self.TxnDate = None #

        #
        self.Memo = None #

        #
        self.Address = empty_class() #

        #
        self.Address.Addr1 = None #

        #
        self.Address.Addr2 = None #

        #
        self.Address.Addr3 = None #

        #
        self.Address.Addr4 = None #

        #
        self.Address.Addr5 = None #

        #
        self.Address.City = None #

        #
        self.Address.State = None #

        #
        self.Address.PostalCode = None #

        #
        self.Address.Country = None #

        #
        self.Address.Note = None #

        #
        self.IsToBePrinted = None #

        #
        self.ExchangeRate = None #

        #
        self.ApplyCheckToTxnAdd = empty_class() #

        #
        self.ApplyCheckToTxnAdd.TxnID = None #

        #
        self.ApplyCheckToTxnAdd.Amount = None #

        #
        self.ExpenseLineAdd = empty_class()#

        #
        self.ExpenseLineAdd.AccountRef = empty_class() #

        #
        self.ExpenseLineAdd.AccountRef.ListID = None #

        #
        self.ExpenseLineAdd.AccountRef.FullName = None #

        #
        self.ExpenseLineAdd.Amount = None #

        #
        self.ExpenseLineAdd.Memo = None #

        #
        self.ExpenseLineAdd.CustomerRef = empty_class() #

        #
        self.ExpenseLineAdd.CustomerRef.ListID = None #

        #
        self.ExpenseLineAdd.CustomerRef.FullName = None #

        #
        self.ExpenseLineAdd.ClassRef = empty_class() #

        #
        self.ExpenseLineAdd.ClassRef.ListID = None #

        #
        self.ExpenseLineAdd.ClassRef.FullName = None #

        #
        self.ExpenseLineAdd.BillableStatus = None #

        #
        self.ExpenseLineAdd.SalesRepRef = empty_class() #

        #
        self.ExpenseLineAdd.SalesRepRef.ListID = None #

        #
        self.ExpenseLineAdd.SalesRepRef.FullName = None #

        #
        self.ExpenseLineAdd.DataExt = empty_class() #

        #
        self.ExpenseLineAdd.DataExt.OwnerID = None #

        #
        self.ExpenseLineAdd.DataExt.DataExtName = None #

        #
        self.ExpenseLineAdd.DataExt.DataExtValue = None #

        #
        self.ItemLineAdd = empty_class() #

        #
        self.ItemLineAdd.ItemRef = empty_class() #

        #
        self.ItemLineAdd.ItemRef.ListID = None #

        #
        self.ItemLineAdd.ItemRef.FullName = None #

        #
        self.ItemLineAdd.InventorySiteRef = empty_class() #

        #
        self.ItemLineAdd.InventorySiteRef.ListID = None #

        #
        self.ItemLineAdd.InventorySiteRef.FullName = None #

        #
        self.ItemLineAdd.InventorySiteLocationRef = empty_class() #

        #
        self.ItemLineAdd.InventorySiteLocationRef.ListID = None #

        #
        self.ItemLineAdd.InventorySiteLocationRef.FullName = None #

        #
        self.ItemLineAdd.SerialNumber = None #

        #
        self.ItemLineAdd.LotNumber = None #

        #
        self.ItemLineAdd.Desc = None #

        #
        self.ItemLineAdd.Quantity = None #

        #
        self.ItemLineAdd.UnitOfMeasure = None #

        #
        self.ItemLineAdd.Cost = None #

        #
        self.ItemLineAdd.Amount = None #

        #
        self.ItemLineAdd.CustomerRef = empty_class() #

        #
        self.ItemLineAdd.CustomerRef.ListID = None #

        #
        self.ItemLineAdd.CustomerRef.FullName = None #

        #
        self.ItemLineAdd.ClassRef = empty_class() #

        #
        self.ItemLineAdd.ClassRef.ListID = None #

        #
        self.ItemLineAdd.ClassRef.FullName = None #

        #
        self.ItemLineAdd.BillableStatus = None #

        #
        self.ItemLineAdd.OverrideItemAccountRef = empty_class() #

        #
        self.ItemLineAdd.OverrideItemAccountRef.ListID = None #

        #
        self.ItemLineAdd.OverrideItemAccountRef.FullName = None #

        #
        self.ItemLineAdd.SalesRepRef = empty_class() #

        #
        self.ItemLineAdd.SalesRepRef.ListID = None #

        #
        self.ItemLineAdd.SalesRepRef.FullName = None #

        #
        self.ItemLineAdd.DataExt = empty_class() #

        #
        self.ItemLineAdd.DataExt.OwnerID = None #

        #
        self.ItemLineAdd.DataExt.DataExtName = None #

        #
        self.ItemLineAdd.DataExt.DataExtValue = None #

        #
        self.ItemGroupLineAdd = empty_class() #

        #
        self.ItemGroupLineAdd.ItemGroupRef = empty_class() #

        #
        self.ItemGroupLineAdd.ItemGroupRef.ListID = None #

        #
        self.ItemGroupLineAdd.ItemGroupRef.FullName = None #

        #
        self.ItemGroupLineAdd.Quantity = None #

        #
        self.ItemGroupLineAdd.UnitOfMeasure = None #

        #
        self.ItemGroupLineAdd.InventorySiteRef = empty_class() #

        #
        self.ItemGroupLineAdd.InventorySiteRef.ListID = None #

        #
        self.ItemGroupLineAdd.InventorySiteRef.FullName = None #

        #
        self.ItemGroupLineAdd.InventorySiteLocationRef = empty_class() #

        #
        self.ItemGroupLineAdd.InventorySiteLocationRef.ListID = None #

        #
        self.ItemGroupLineAdd.InventorySiteLocationRef.FullName = None #

        #
        self.ItemGroupLineAdd.DataExt = empty_class() #

        #
        self.ItemGroupLineAdd.DataExt.OwnerID = None #

        #
        self.ItemGroupLineAdd.DataExt.DataExtName = None #

        #
        self.ItemGroupLineAdd.DataExt.DataExtValue = None #

    def set_AccountQueryRq_attributes(self):
        '''
        WARNING NEED TO CHECK ATTRIBUTES
        My IDE sure does hate me doing this, but it sure does work
        Any suggestions on a better way to do this???
        '''
        self.qbcom.QBXMLMsgsRq.set('onError', self.onError)
        self.qbcom.AccountQueryRq = ET.SubElement(self.qbcom.QBXMLMsgsRq, self.request_ID)
        self.qbcom.AccountQueryRq.set('metaData', self.metaData)
        if self.iterator:
            self.qbcom.AccountQueryRq.set('iterator', self.iterator)
        if self.ListID:
            self.qbcom.ListID = ET.SubElement(self.qbcom.AccountQueryRq, 'ListID')
            self.qbcom.ListID.text = self.ListID
        elif self.FullName:
            self.qbcom.FullName = ET.SubElement(self.qbcom.AccountQueryRq, 'FullName')
            self.qbcom.FullName.text = self.FullName
        else:
            if self.MaxReturned:
                self.qbcom.MaxReturned = ET.SubElement(self.qbcom.AccountQueryRq, 'MaxReturned')
                self.qbcom.MaxReturned.text = self.MaxReturned
            if self.ActiveStatus:
                self.qbcom.ActiveStatus = ET.SubElement(self.qbcom.AccountQueryRq, 'ActiveStatus')
                self.qbcom.ActiveStatus.text = self.ActiveStatus
            if self.FromModifiedDate:
                self.qbcom.FromModifiedDate = ET.SubElement(self.qbcom.AccountQueryRq, 'FromModifiedDate')
                self.qbcom.FromModifiedDate.text = self.FromModifiedDate
            if self.ToModifiedDate:
                self.qbcom.ToModifiedDate = ET.SubElement(self.qbcom.AccountQueryRq, 'ToModifiedDate')
                self.qbcom.ToModifiedDate.text = self.ToModifiedDate
            if self.NameFilter.MatchCriterion and self.Namefilter.Name:
                self.qbcom.NameFilter = ET.SubElement(self.qbcom.AccountQueryRq, 'NameFilter')
                self.qbcom.NameFilter.text = self.NameFilter
                self.qbcom.MatchCriterion = ET.SubElement(self.qbcom.NameFilter, 'MatchCriterion')
                self.qbcom.MatchCriterion.text = self.MatchCriterion
                self.qbcom.Name = ET.SubElement(self.qbcom.NameFilter, 'Name')
                self.qbcom.Name.text = self.Name
            elif self.NameRangeFilter.FromName and self.NameRangeFilter.ToName:
                self.qbcom.NameRangeFilter = ET.SubElement(self.qbcom.AccountQueryRq, 'NameRangeFilter')
                self.qbcom.NameRangeFilter.text = self.NameRangeFilter
                self.qbcom.FromName = ET.SubElement(self.qbcom.NameRangeFilter, 'FromName')
                self.qbcom.FromName.text = self.FromName
                self.qbcom.ToName = ET.SubElement(self.qbcom.NameRangeFilter, 'ToName')
                self.qbcom.ToName.text = self.ToName
            if self.TotalBalanceFilter.Operator and self.TotalBalanceFilter.Amount:
                self.qbcom.TotalBalanceFilter = ET.SubElement(self.qbcom.AccountQueryRq, 'TotalBalanceFilter')
                self.qbcom.TotalBalanceFilter.text = self.TotalBalanceFilter
                self.qbcom.Operator = ET.SubElement(self.qbcom.TotalBalanceFilter, 'Operator')
                self.qbcom.Operator.text = self.Operator
                self.qbcom.Amount = ET.SubElement(self.qbcom.TotalBalanceFilter, 'Amount')
                self.qbcom.Amount.text = self.Amount
            if self.CurrencyFilter.ListID:
                self.qbcom.CurrencyFilter = ET.SubElement(self.qbcom.AccountQueryRq, 'CurrencyFilter')
                self.qbcom.CurrencyFilter.text = self.CurrencyFilter
                self.qbcom.ListID = ET.SubElement(self.qbcom.CurrencyFilter, 'ListID')
                self.qbcom.ListID.text = self.ListID
            elif self.CurrencyFilter.FullName:
                self.qbcom.CurrencyFilter = ET.SubElement(self.qbcom.AccountQueryRq, 'CurrencyFilter')
                self.qbcom.CurrencyFilter.text = self.CurrencyFilter
                self.qbcom.FullName = ET.SubElement(self.qbcom.CurrencyFilter, 'FullName')
                self.qbcom.FullName.text = self.FullName
            if self.ClassFilter.ListID:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.AccountQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.ListID = ET.SubElement(self.qbcom.ClassFilter, 'ListID')
                self.qbcom.ListID.text = self.ListID
            elif self.ClassFilter.FullName:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.AccountQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.FullName = ET.SubElement(self.qbcom.ClassFilter, 'FullName')
                self.qbcom.FullName.text = self.FullName
            elif self.ClassFilter.ListIDWithChildren:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.AccountQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.ListIDWithChildren = ET.SubElement(self.qbcom.ClassFilter, 'ListIDWithChildren')
                self.qbcom.ListIDWithChildren.text = self.ListIDWithChildren
            elif self.ClassFilter.FullNameWithChildren:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.AccountQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.FullNameWithChildren = ET.SubElement(self.qbcom.ClassFilter, 'FullNameWithChildren')
                self.qbcom.FullNameWithChildren.text = self.FullNameWithChildren
        if self.IncludeRetElement:
            for item in self.IncludeRetElemenet:
                self.qbcom.IncludeRetElement = ET.SubElement(self.qbcom.AccountQueryRq, 'IncludeRetElement')
                self.qbcom.IncludeRetElement.text = item
        if self.OwnerID:
                self.qbcom.OwnerID = ET.SubElement(self.qbcom.AccountQueryRq, 'OwnerID')
                self.qbcom.OwnerID.text = self.OwnerID

    def set_CheckQueryRq_attributes(self):
        '''
        My IDE sure does hate me doing this, but it sure does work
        Any suggestions on a better way to do this???
        '''
        self.qbcom.QBXMLMsgsRq.set('onError', self.onError)
        self.qbcom.CustomerQueryRq = ET.SubElement(self.qbcom.QBXMLMsgsRq, self.request_ID)
        self.qbcom.CustomerQueryRq.set('metaData', self.metaData)
        if self.iterator:
            self.qbcom.CustomerQueryRq.set('iterator', self.iterator)
        if self.ListID:
            self.qbcom.ListID = ET.SubElement(self.qbcom.CustomerQueryRq, 'ListID')
            self.qbcom.ListID.text = self.ListID
        elif self.FullName:
            self.qbcom.FullName = ET.SubElement(self.qbcom.CustomerQueryRq, 'FullName')
            self.qbcom.FullName.text = self.FullName
        else:
            if self.MaxReturned:
                self.qbcom.MaxReturned = ET.SubElement(self.qbcom.CustomerQueryRq, 'MaxReturned')
                self.qbcom.MaxReturned.text = self.MaxReturned
            if self.ActiveStatus:
                self.qbcom.ActiveStatus = ET.SubElement(self.qbcom.CustomerQueryRq, 'ActiveStatus')
                self.qbcom.ActiveStatus.text = self.ActiveStatus
            if self.FromModifiedDate:
                self.qbcom.FromModifiedDate = ET.SubElement(self.qbcom.CustomerQueryRq, 'FromModifiedDate')
                self.qbcom.FromModifiedDate.text = self.FromModifiedDate
            if self.ToModifiedDate:
                self.qbcom.ToModifiedDate = ET.SubElement(self.qbcom.CustomerQueryRq, 'ToModifiedDate')
                self.qbcom.ToModifiedDate.text = self.ToModifiedDate
            if self.NameFilter.MatchCriterion and self.Namefilter.Name:
                self.qbcom.NameFilter = ET.SubElement(self.qbcom.CustomerQueryRq, 'NameFilter')
                self.qbcom.NameFilter.text = self.NameFilter
                self.qbcom.MatchCriterion = ET.SubElement(self.qbcom.NameFilter, 'MatchCriterion')
                self.qbcom.MatchCriterion.text = self.MatchCriterion
                self.qbcom.Name = ET.SubElement(self.qbcom.NameFilter, 'Name')
                self.qbcom.Name.text = self.Name
            elif self.NameRangeFilter.FromName and self.NameRangeFilter.ToName:
                self.qbcom.NameRangeFilter = ET.SubElement(self.qbcom.CustomerQueryRq, 'NameRangeFilter')
                self.qbcom.NameRangeFilter.text = self.NameRangeFilter
                self.qbcom.FromName = ET.SubElement(self.qbcom.NameRangeFilter, 'FromName')
                self.qbcom.FromName.text = self.FromName
                self.qbcom.ToName = ET.SubElement(self.qbcom.NameRangeFilter, 'ToName')
                self.qbcom.ToName.text = self.ToName
            if self.TotalBalanceFilter.Operator and self.TotalBalanceFilter.Amount:
                self.qbcom.TotalBalanceFilter = ET.SubElement(self.qbcom.CustomerQueryRq, 'TotalBalanceFilter')
                self.qbcom.TotalBalanceFilter.text = self.TotalBalanceFilter
                self.qbcom.Operator = ET.SubElement(self.qbcom.TotalBalanceFilter, 'Operator')
                self.qbcom.Operator.text = self.Operator
                self.qbcom.Amount = ET.SubElement(self.qbcom.TotalBalanceFilter, 'Amount')
                self.qbcom.Amount.text = self.Amount
            if self.CurrencyFilter.ListID:
                self.qbcom.CurrencyFilter = ET.SubElement(self.qbcom.CustomerQueryRq, 'CurrencyFilter')
                self.qbcom.CurrencyFilter.text = self.CurrencyFilter
                self.qbcom.ListID = ET.SubElement(self.qbcom.CurrencyFilter, 'ListID')
                self.qbcom.ListID.text = self.ListID
            elif self.CurrencyFilter.FullName:
                self.qbcom.CurrencyFilter = ET.SubElement(self.qbcom.CustomerQueryRq, 'CurrencyFilter')
                self.qbcom.CurrencyFilter.text = self.CurrencyFilter
                self.qbcom.FullName = ET.SubElement(self.qbcom.CurrencyFilter, 'FullName')
                self.qbcom.FullName.text = self.FullName
            if self.ClassFilter.ListID:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.CustomerQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.ListID = ET.SubElement(self.qbcom.ClassFilter, 'ListID')
                self.qbcom.ListID.text = self.ListID
            elif self.ClassFilter.FullName:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.CustomerQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.FullName = ET.SubElement(self.qbcom.ClassFilter, 'FullName')
                self.qbcom.FullName.text = self.FullName
            elif self.ClassFilter.ListIDWithChildren:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.CustomerQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.ListIDWithChildren = ET.SubElement(self.qbcom.ClassFilter, 'ListIDWithChildren')
                self.qbcom.ListIDWithChildren.text = self.ListIDWithChildren
            elif self.ClassFilter.FullNameWithChildren:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.CustomerQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.FullNameWithChildren = ET.SubElement(self.qbcom.ClassFilter, 'FullNameWithChildren')
                self.qbcom.FullNameWithChildren.text = self.FullNameWithChildren
        if self.IncludeRetElement:
            for item in self.IncludeRetElemenet:
                self.qbcom.IncludeRetElement = ET.SubElement(self.qbcom.CustomerQueryRq, 'IncludeRetElement')
                self.qbcom.IncludeRetElement.text = item
        if self.OwnerID:
                self.qbcom.OwnerID = ET.SubElement(self.qbcom.CustomerQueryRq, 'OwnerID')
                self.qbcom.OwnerID.text = self.OwnerID

    def set_CustomerQueryRq_attributes(self):
        '''
        My IDE sure does hate me doing this, but it sure does work
        Any suggestions on a better way to do this???
        '''
        if self.onError:
            self.qbcom.QBXMLMsgsRq.set('onError', self.onError)
        self.qbcom.CustomerQueryRq = ET.SubElement(self.qbcom.QBXMLMsgsRq, self.request_ID)
        if self.metaData:
            self.qbcom.CustomerQueryRq.set('metaData', self.metaData)
        if self.iterator:
            self.qbcom.CustomerQueryRq.set('iterator', self.iterator)
        if self.ListID:
            self.qbcom.ListID = ET.SubElement(self.qbcom.CustomerQueryRq, 'ListID')
            self.qbcom.ListID.text = self.ListID
        elif self.FullName:
            self.qbcom.FullName = ET.SubElement(self.qbcom.CustomerQueryRq, 'FullName')
            self.qbcom.FullName.text = self.FullName
        else:
            if self.MaxReturned:
                self.qbcom.MaxReturned = ET.SubElement(self.qbcom.CustomerQueryRq, 'MaxReturned')
                self.qbcom.MaxReturned.text = self.MaxReturned
            if self.ActiveStatus:
                self.qbcom.ActiveStatus = ET.SubElement(self.qbcom.CustomerQueryRq, 'ActiveStatus')
                self.qbcom.ActiveStatus.text = self.ActiveStatus
            if self.FromModifiedDate:
                self.qbcom.FromModifiedDate = ET.SubElement(self.qbcom.CustomerQueryRq, 'FromModifiedDate')
                self.qbcom.FromModifiedDate.text = self.FromModifiedDate
            if self.ToModifiedDate:
                self.qbcom.ToModifiedDate = ET.SubElement(self.qbcom.CustomerQueryRq, 'ToModifiedDate')
                self.qbcom.ToModifiedDate.text = self.ToModifiedDate
            if self.NameFilter.MatchCriterion and self.Namefilter.Name:
                self.qbcom.NameFilter = ET.SubElement(self.qbcom.CustomerQueryRq, 'NameFilter')
                self.qbcom.NameFilter.text = self.NameFilter
                self.qbcom.MatchCriterion = ET.SubElement(self.qbcom.NameFilter, 'MatchCriterion')
                self.qbcom.MatchCriterion.text = self.MatchCriterion
                self.qbcom.Name = ET.SubElement(self.qbcom.NameFilter, 'Name')
                self.qbcom.Name.text = self.Name
            elif self.NameRangeFilter.FromName and self.NameRangeFilter.ToName:
                self.qbcom.NameRangeFilter = ET.SubElement(self.qbcom.CustomerQueryRq, 'NameRangeFilter')
                self.qbcom.NameRangeFilter.text = self.NameRangeFilter
                self.qbcom.FromName = ET.SubElement(self.qbcom.NameRangeFilter, 'FromName')
                self.qbcom.FromName.text = self.FromName
                self.qbcom.ToName = ET.SubElement(self.qbcom.NameRangeFilter, 'ToName')
                self.qbcom.ToName.text = self.ToName
            if self.TotalBalanceFilter.Operator and self.TotalBalanceFilter.Amount:
                self.qbcom.TotalBalanceFilter = ET.SubElement(self.qbcom.CustomerQueryRq, 'TotalBalanceFilter')
                self.qbcom.TotalBalanceFilter.text = self.TotalBalanceFilter
                self.qbcom.Operator = ET.SubElement(self.qbcom.TotalBalanceFilter, 'Operator')
                self.qbcom.Operator.text = self.Operator
                self.qbcom.Amount = ET.SubElement(self.qbcom.TotalBalanceFilter, 'Amount')
                self.qbcom.Amount.text = self.Amount
            if self.CurrencyFilter.ListID:
                self.qbcom.CurrencyFilter = ET.SubElement(self.qbcom.CustomerQueryRq, 'CurrencyFilter')
                self.qbcom.CurrencyFilter.text = self.CurrencyFilter
                self.qbcom.ListID = ET.SubElement(self.qbcom.CurrencyFilter, 'ListID')
                self.qbcom.ListID.text = self.ListID
            elif self.CurrencyFilter.FullName:
                self.qbcom.CurrencyFilter = ET.SubElement(self.qbcom.CustomerQueryRq, 'CurrencyFilter')
                self.qbcom.CurrencyFilter.text = self.CurrencyFilter
                self.qbcom.FullName = ET.SubElement(self.qbcom.CurrencyFilter, 'FullName')
                self.qbcom.FullName.text = self.FullName
            if self.ClassFilter.ListID:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.CustomerQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.ListID = ET.SubElement(self.qbcom.ClassFilter, 'ListID')
                self.qbcom.ListID.text = self.ListID
            elif self.ClassFilter.FullName:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.CustomerQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.FullName = ET.SubElement(self.qbcom.ClassFilter, 'FullName')
                self.qbcom.FullName.text = self.FullName
            elif self.ClassFilter.ListIDWithChildren:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.CustomerQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.ListIDWithChildren = ET.SubElement(self.qbcom.ClassFilter, 'ListIDWithChildren')
                self.qbcom.ListIDWithChildren.text = self.ListIDWithChildren
            elif self.ClassFilter.FullNameWithChildren:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.CustomerQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.FullNameWithChildren = ET.SubElement(self.qbcom.ClassFilter, 'FullNameWithChildren')
                self.qbcom.FullNameWithChildren.text = self.FullNameWithChildren
        if self.IncludeRetElement:
            for item in self.IncludeRetElemenet:
                self.qbcom.IncludeRetElement = ET.SubElement(self.qbcom.CustomerQueryRq, 'IncludeRetElement')
                self.qbcom.IncludeRetElement.text = item
        if self.OwnerID:
                self.qbcom.OwnerID = ET.SubElement(self.qbcom.CustomerQueryRq, 'OwnerID')
                self.qbcom.OwnerID.text = self.OwnerID

    def set_VendorQueryRq_attributes(self):
        '''
        My IDE sure does hate me doing this, but it sure does work
        Any suggestions on a better way to do this???
        '''
        if self.onError:
            self.qbcom.QBXMLMsgsRq.set('onError', self.onError)
        self.qbcom.VendorQueryRq = ET.SubElement(self.qbcom.QBXMLMsgsRq, self.request_ID)
        if self.metaData:
            self.qbcom.VendorQueryRq.set('metaData', self.metaData)
        if self.iterator:
            self.qbcom.VendorQueryRq.set('iterator', self.iterator)
        if self.ListID:
            self.qbcom.ListID = ET.SubElement(self.qbcom.VendorQueryRq, 'ListID')
            self.qbcom.ListID.text = self.ListID
        elif self.FullName:
            self.qbcom.FullName = ET.SubElement(self.qbcom.VendorQueryRq, 'FullName')
            self.qbcom.FullName.text = self.FullName
        else:
            if self.MaxReturned:
                self.qbcom.MaxReturned = ET.SubElement(self.qbcom.VendorQueryRq, 'MaxReturned')
                self.qbcom.MaxReturned.text = self.MaxReturned
            if self.ActiveStatus:
                self.qbcom.ActiveStatus = ET.SubElement(self.qbcom.VendorQueryRq, 'ActiveStatus')
                self.qbcom.ActiveStatus.text = self.ActiveStatus
            if self.FromModifiedDate:
                self.qbcom.FromModifiedDate = ET.SubElement(self.qbcom.VendorQueryRq, 'FromModifiedDate')
                self.qbcom.FromModifiedDate.text = self.FromModifiedDate
            if self.ToModifiedDate:
                self.qbcom.ToModifiedDate = ET.SubElement(self.qbcom.VendorQueryRq, 'ToModifiedDate')
                self.qbcom.ToModifiedDate.text = self.ToModifiedDate
            if self.NameFilter.MatchCriterion and self.Namefilter.Name:
                self.qbcom.NameFilter = ET.SubElement(self.qbcom.VendorQueryRq, 'NameFilter')
                self.qbcom.NameFilter.text = self.NameFilter
                self.qbcom.MatchCriterion = ET.SubElement(self.qbcom.NameFilter, 'MatchCriterion')
                self.qbcom.MatchCriterion.text = self.MatchCriterion
                self.qbcom.Name = ET.SubElement(self.qbcom.NameFilter, 'Name')
                self.qbcom.Name.text = self.Name
            elif self.NameRangeFilter.FromName and self.NameRangeFilter.ToName:
                self.qbcom.NameRangeFilter = ET.SubElement(self.qbcom.VendorQueryRq, 'NameRangeFilter')
                self.qbcom.NameRangeFilter.text = self.NameRangeFilter
                self.qbcom.FromName = ET.SubElement(self.qbcom.NameRangeFilter, 'FromName')
                self.qbcom.FromName.text = self.FromName
                self.qbcom.ToName = ET.SubElement(self.qbcom.NameRangeFilter, 'ToName')
                self.qbcom.ToName.text = self.ToName
            if self.TotalBalanceFilter.Operator and self.TotalBalanceFilter.Amount:
                self.qbcom.TotalBalanceFilter = ET.SubElement(self.qbcom.VendorQueryRq, 'TotalBalanceFilter')
                self.qbcom.TotalBalanceFilter.text = self.TotalBalanceFilter
                self.qbcom.Operator = ET.SubElement(self.qbcom.TotalBalanceFilter, 'Operator')
                self.qbcom.Operator.text = self.Operator
                self.qbcom.Amount = ET.SubElement(self.qbcom.TotalBalanceFilter, 'Amount')
                self.qbcom.Amount.text = self.Amount
            if self.CurrencyFilter.ListID:
                self.qbcom.CurrencyFilter = ET.SubElement(self.qbcom.VendorQueryRq, 'CurrencyFilter')
                self.qbcom.CurrencyFilter.text = self.CurrencyFilter
                self.qbcom.ListID = ET.SubElement(self.qbcom.CurrencyFilter, 'ListID')
                self.qbcom.ListID.text = self.ListID
            elif self.CurrencyFilter.FullName:
                self.qbcom.CurrencyFilter = ET.SubElement(self.qbcom.VendorQueryRq, 'CurrencyFilter')
                self.qbcom.CurrencyFilter.text = self.CurrencyFilter
                self.qbcom.FullName = ET.SubElement(self.qbcom.CurrencyFilter, 'FullName')
                self.qbcom.FullName.text = self.FullName
            if self.ClassFilter.ListID:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.VendorQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.ListID = ET.SubElement(self.qbcom.ClassFilter, 'ListID')
                self.qbcom.ListID.text = self.ListID
            elif self.ClassFilter.FullName:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.VendorQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.FullName = ET.SubElement(self.qbcom.ClassFilter, 'FullName')
                self.qbcom.FullName.text = self.FullName
            elif self.ClassFilter.ListIDWithChildren:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.VendorQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.ListIDWithChildren = ET.SubElement(self.qbcom.ClassFilter, 'ListIDWithChildren')
                self.qbcom.ListIDWithChildren.text = self.ListIDWithChildren
            elif self.ClassFilter.FullNameWithChildren:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.VendorQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.FullNameWithChildren = ET.SubElement(self.qbcom.ClassFilter, 'FullNameWithChildren')
                self.qbcom.FullNameWithChildren.text = self.FullNameWithChildren
        if self.IncludeRetElement:
            for item in self.IncludeRetElemenet:
                self.qbcom.IncludeRetElement = ET.SubElement(self.qbcom.VendorQueryRq, 'IncludeRetElement')
                self.qbcom.IncludeRetElement.text = item
        if self.OwnerID:
                self.qbcom.OwnerID = ET.SubElement(self.qbcom.VendorQueryRq, 'OwnerID')
                self.qbcom.OwnerID.text = self.OwnerID

    def set_CheckAddRq_attributes(self):
        '''
        My IDE sure does hate me doing this, but it sure does work
        Any suggestions on a better way to do this???
        '''
        self.qbcom.QBXMLMsgsRq.set('onError', self.onError)
        self.qbcom.CheckAddRq = ET.SubElement(self.qbcom.QBXMLMsgsRq, 'CheckAddRq')
        self.qbcom.CheckAdd = ET.SubElement(self.qbcom.CheckAddRq, 'CheckAdd')
        if self.AccountRef.ListID or self.AccountRef.FullName:
            self.qbcom.AccountRef = ET.SubElement(self.qbcom.CheckAdd, 'AccountRef')
            if self.AccountRef.ListID:
                self.qbcom.AccountRef_ListID = ET.SubElement(self.qbcom.AccountRef, 'ListID')
                self.qbcom.AccountRef_ListID.text = self.AccountRef.ListID
            elif self.AccountRef.FullName:
                self.qbcom.AccountRef_FullName = ET.SubElement(self.qbcom.AccountRef, 'FullName')
                self.qbcom.AccountRef_FullName.text = self.AccountRef.FullName
        if self.PayeeEntityRef.ListID or self.PayeeEntityRef.FullName:
            self.qbcom.PayeeEntityRef = ET.SubElement(self.qbcom.CheckAdd, 'PayeeEntityRef')
            self.qbcom.PayeeEntityRef_ListID = ET.SubElement(self.qbcom.PayeeEntityRef, 'ListID')
            self.qbcom.PayeeEntityRef_ListID.text = self.PayeeEntityRef.ListID
            self.qbcom.PayeeEntityRef_FullName = ET.SubElement(self.qbcom.PayeeEntityRef, 'FullName')
            self.qbcom.PayeeEntityRef_FullName.text = self.PayeeEntityRef.FullName
        if self.RefNumber:
            self.qbcom.RefNumber = ET.SubElement(self.qbcom.CheckAdd, 'RefNumber')
            self.qbcom.RefNumber.text = self.RefNumber
        if self.TxnDate:
            self.qbcom.TxnDate = ET.SubElement(self.qbcom.CheckAdd, 'TxnDate')
            self.qbcom.TxnDate.text = self.TxnDate
        if self.Memo:
            self.qbcom.Memo = ET.SubElement(self.qbcom.CheckAdd, 'Memo')
            self.qbcom.Memo.text = self.Memo
        if (self.Address.Addr1 and
                self.Address.Addr2 and
                self.Address.Addr3 and
                self.Address.Addr4 and
                self.Address.Addr5 and
                self.Address.City and
                self.Address.State and
                self.Address.PostalCode):
            self.qbcom.Address = ET.SubElement(self.qbcom.CheckAdd, 'Address')
            self.qbcom.Address = ET.SubElement(self.qbcom.Address, 'Addr1')
            self.qbcom.Address_Addr1.text = self.Address.Addr1
            self.qbcom.Address = ET.SubElement(self.qbcom.Address, 'Addr2')
            self.qbcom.Address_Addr2.text = self.Address.Addr2
            self.qbcom.Address = ET.SubElement(self.qbcom.Address, 'Addr3')
            self.qbcom.Address_Addr3.text = self.Address.Addr3
            self.qbcom.Address = ET.SubElement(self.qbcom.Address, 'Addr4')
            self.qbcom.Address_Addr4.text = self.Address.Addr4
            self.qbcom.Address = ET.SubElement(self.qbcom.Address, 'Addr5')
            self.qbcom.Address_Addr5.text = self.Address.Addr5
            self.qbcom.Address = ET.SubElement(self.qbcom.Address, 'City')
            self.qbcom.Address_City.text = self.Address.City
            self.qbcom.Address = ET.SubElement(self.qbcom.Address, 'State')
            self.qbcom.Address_State.text = self.Address.State
            self.qbcom.Address = ET.SubElement(self.qbcom.Address, 'PostalCode')
            self.qbcom.Address_PostalCode.text = self.Address.PostalCode
            if self.Address.Country:
                self.qbcom.Address = ET.SubElement(self.qbcom.Address, 'Country')
                self.qbcom.Address_Country.text = self.Address.Country
            if self.Address.Note:
                self.qbcom.Address = ET.SubElement(self.qbcom.Address, 'Note')
                self.qbcom.Address_Note.text = self.Address.Note
        if self.IsToBePrinted:
            self.qbcom.IsToBePrinted = ET.SubElement(self.qbcom.CheckAdd, 'IsToBePrinted')
            self.qbcom.IsToBePrinted.text = self.IsToBePrinted
        if self.ExchangeRate:
            self.qbcom.ExchangeRate = ET.SubElement(self.qbcom.CheckAdd, 'ExchangeRate')
            self.qbcom.ExchangeRate.text = self.ExchangeRate
        if self.ExternalGUID:
            self.qbcom.ExternalGUID = ET.SubElement(self.qbcom.CheckAdd, 'ExternalGUID')
            self.qbcom.ExternalGUID.text = self.ExternalGUID
        if self.ApplyCheckToTxnAdd.TxnID or self.ApplyCheckToTxnAdd.Amount:
            self.qbcom.ApplyCheckToTxnAdd = ET.SubElement(self.qbcom.CheckAdd, 'ApplyCheckToTxnAdd')
            self.qbcom.ApplyCheckToTxnAdd_TxnID = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'TxnID')
            self.qbcom.ApplyCheckToTxnAdd_TxnID.text = self.ApplyCheckToTxnAdd.TxnID
            self.qbcom.ApplyCheckToTxnAdd_Amount = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'Amount')
            self.qbcom.ApplyCheckToTxnAdd_Amount.text = self.ApplyCheckToTxnAdd.Amount
        if (self.ExpenseLineAdd.AccountRef.ListID or 
                self.ExpenseLineAdd.AccountRef.FullName or
                self.ExpenseLineAdd.ClassRef.ListID or
                self.ExpenseLineAdd.ClassRef.FullName or
                self.ExpenseLineAdd.BillableStatus or
                self.ExpenseLineAdd.SalesRepRef.ListID or
                self.ExpenseLineAdd.SalesRepRef.FullName or
                self.ExpenseLineAdd.DataExt.OwnerID or
                self.ExpenseLineAdd.DataExt.DataExtName or
                self.ExpenseLineAdd.DataExt.DataExtValue):
            self.qbcom.ExpenseLineAdd = ET.SubElement(self.qbcom.CheckAdd, 'ExpenseLineAdd')
            if self.ExpenseLineAdd.AccountRef.ListID or self.ExpenseLineAdd.AccountRef.FullName:
                self.qbcom.ExpenseLineAdd_AccountRef = ET.SubElement(self.qbcom.ExpenseLineAdd, 'AccountRef')
                self.qbcom.ExpenseLineAdd_AccountRef_ListID = ET.SubElement(self.qbcom.ExpenseLineAdd_AccountRef, 'ListID')
                self.qbcom.ExpenseLineAdd_AccountRef_ListID.text = self.ExpenseLineAdd.AccountRef.ListID
                self.qbcom.ExpenseLineAdd_AccountRef_FullName = ET.SubElement(self.qbcom.ExpenseLineAdd_AccountRef, 'FullName')
                self.qbcom.ExpenseLineAdd_AccountRef_FullName.text = self.ExpenseLineAdd.AccountRef.FullName
            if self.ExpenseLineAdd.Amount:
                self.qbcom.ExpenseLineAdd_Amount = ET.SubElement(self.qbcom.ExpenseLineAdd, 'Amount')
                self.qbcom.ExpenseLineAdd_Amount.text = self.ExpenseLineAdd.Amount
            if self.ExpenseLineAdd.Memo:
                self.qbcom.ExpenseLineAdd_Memo = ET.SubElement(self.qbcom.ExpenseLineAdd, 'Memo')
                self.qbcom.ExpenseLineAdd_Memo.text = self.ExpenseLineAdd.Memo
            if self.ExpenseLineAdd.CustomerRef.ListID or self.ExpenseLineAdd.CustomerRef.FullName:
                self.qbcom.ExpenseLineAdd_CustomerRef = ET.SubElement(self.qbcom.ExpenseLineAdd, 'CustomerRef')
                self.qbcom.ExpenseLineAdd_CustomerRef_ListID = ET.SubElement(self.qbcom.ExpenseLineAdd_CustomerRef, 'ListID')
                self.qbcom.ExpenseLineAdd_CustomerRef_ListID.text = self.ExpenseLineAdd.CustomerRef.ListID
                self.qbcom.ExpenseLineAdd_CustomerRef_FullName = ET.SubElement(self.qbcom.ExpenseLineAdd_CustomerRef, 'FullName')
                self.qbcom.ExpenseLineAdd_CustomerRef_FullName.text = self.ExpenseLineAdd.CustomerRef.FullName
            if self.ExpenseLineAdd.ClassRef.ListID or self.ExpenseLineAdd.ClassRef.FullName:
                self.qbcom.ExpenseLineAdd_ClassRef = ET.SubElement(self.qbcom.ExpenseLineAdd, 'ClassRef')
                self.qbcom.ExpenseLineAdd_ClassRef_ListID = ET.SubElement(self.qbcom.ExpenseLineAdd_ClassRef, 'ListID')
                self.qbcom.ExpenseLineAdd_ClassRef_ListID.text = self.ExpenseLineAdd.ClassRef.ListID
                self.qbcom.ExpenseLineAdd_ClassRef_FullName = ET.SubElement(self.qbcom.ExpenseLineAdd_ClassRef, 'FullName')
                self.qbcom.ExpenseLineAdd_ClassRef_FullName.text = self.ExpenseLineAdd.ClassRef.FullName
            if self.ExpenseLineAdd.BillableStatus:
                self.qbcom.ExpenseLineAdd_BillableStatus = ET.SubElement(self.qbcom.ExpenseLineAdd, 'BillableStatus')
                self.qbcom.ExpenseLineAdd_BillableStatus.text = self.ExpenseLineAdd.BillableStatus
            if self.ExpenseLineAdd.SalesRepRef.ListID or self.ExpenseLineAdd.SalesRepRef.FullName:
                self.qbcom.ExpenseLineAdd_SalesRepRef = ET.SubElement(self.qbcom.ExpenseLineAdd, 'SalesRepRef')
                self.qbcom.ExpenseLineAdd_SalesRepRef_ListID = ET.SubElement(self.qbcom.ExpenseLineAdd_SalesRepRef, 'ListID')
                self.qbcom.ExpenseLineAdd_SalesRepRef_ListID.text = self.ExpenseLineAdd.SalesRepRef.ListID
                self.qbcom.ExpenseLineAdd_SalesRepRef_FullName = ET.SubElement(self.qbcom.ExpenseLineAdd_SalesRepRef, 'FullName')
                self.qbcom.ExpenseLineAdd_SalesRepRef_FullName.text = self.ExpenseLineAdd.SalesRepRef.FullName
            if (self.ExpenseLineAdd.DataExt.OwnerID or
                    self.ExpenseLineAdd.DataExt.DataExtName or
                    self.ExpenseLineAdd.DataExt.DataExtValue):
                self.qbcom.ExpenseLineAdd_DataExt = ET.SubElement(self.qbcom.ExpenseLineAdd, 'DataExt')
                self.qbcom.ExpenseLineAdd_DataExt_OwnerID = ET.SubElement(self.qbcom.ExpenseLineAdd_DataExt, 'OwnerID')
                self.qbcom.ExpenseLineAdd_DataExt_OwnerID.text = self.ExpenseLineAdd.DataExt.OwnerID
                self.qbcom.ExpenseLineAdd_DataExt_DataExtName = ET.SubElement(self.qbcom.ExpenseLineAdd_DataExt, 'DataExtName')
                self.qbcom.ExpenseLineAdd_DataExt_DataExtName.text = self.ExpenseLineAdd.DataExt.DataExtName
                self.qbcom.ExpenseLineAdd_DataExt_DataExtValue = ET.SubElement(self.qbcom.ExpenseLineAdd_DataExt, 'DataExtValue')
                self.qbcom.ExpenseLineAdd_DataExt_DataExtValue.text = self.ExpenseLineAdd.DataExt.DataExtValue
        if (self.ItemLineAdd.ItemRef.ListID or
                self.ItemLineAdd.ItemRef.FullName or
                self.ItemLineAdd.InventorySiteRef.ListID or
                self.ItemLineAdd.InventorySiteRef.FullName or
                self.ItemLineAdd.InventorySiteLocationRef.ListID or
                self.ItemLineAdd.InventorySiteLocationRef.FullName or
                self.ItemLineAdd.SerialNumber or
                self.ItemLineAdd.LotNumber or
                self.ItemLineAdd.Desc or
                self.ItemLineAdd.Quantity or
                self.ItemLineAdd.UnitOfMeasure or
                self.ItemLineAdd.Cost or
                self.ItemLineAdd.Amount or
                self.ItemLineAdd.CustomerRef.ListID or
                self.ItemLineAdd.CustomerRef.FullName or
                self.ItemLineAdd.ClassRef.ListID or
                self.ItemLineAdd.ClassRef.FullName or
                self.ItemLineAdd.BillableStatus or
                self.ItemLineAdd.OverrideItemAccountRef.ListID or
                self.ItemLineAdd.OverrideItemAccountRef.FullName or
                self.ItemLineAdd.SalesRepRef.ListID or
                self.ItemLineAdd.SalesRepRef.FullName or
                self.ItemLineAdd.DataExt.OwnerID or
                self.ItemLineAdd.DataExt.DataExtName or
                self.ItemLineAdd.DataExt.DataExtValue):
            self.qbcom.ItemLineAdd = ET.SubElement(self.qbcom.CheckAdd, 'ItemLineAdd')
            if self.ItemLineAdd.ItemRef.ListID or self.ItemLineAdd.ItemRef.FullName:
                self.qbcom.ItemLineAdd_ItemRef = ET.SubElement(self.qbcom.CheckAdd, 'ItemRef')
                self.qbcom.ItemLineAdd_ItemRef_ListID = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'ListID')
                self.qbcom.ItemLineAdd_ItemRef_ListID.text = self.ItemLineAdd.ItemRef.ListID
                self.qbcom.ItemLineAdd_ItemRef_FullName = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'FullName')
                self.qbcom.ItemLineAdd_ItemRef_FullName.text = self.ItemLineAdd.ItemRef.FullName
            if self.ItemLineAdd.InventorySiteRef.ListID or self.ItemLineAdd.InventorySiteRef.FullName:
                self.qbcom.ItemLineAdd_InventorySiteRef = ET.SubElement(self.qbcom.CheckAdd, 'InventorySiteRef')
                self.qbcom.ItemLineAdd_InventorySiteRef_ListID = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'ListID')
                self.qbcom.ItemLineAdd_InventorySiteRef_ListID.text = self.ItemLineAdd.InventorySiteRef.ListID
                self.qbcom.ItemLineAdd_InventorySiteRef_FullName = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'FullName')
                self.qbcom.ItemLineAdd_InventorySiteRef_FullName.text = self.ItemLineAdd.InventorySiteRef.FullName
            if self.ItemLineAdd.InventorySiteLocationRef.ListID or self.ItemLineAdd.InventorySiteLocationRef.FullName:
                self.qbcom.ItemLineAdd_InventorySiteLocationRef = ET.SubElement(self.qbcom.CheckAdd, 'InventorySiteLocationRef')
                self.qbcom.ItemLineAdd_InventorySiteLocationRef_ListID = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'ListID')
                self.qbcom.ItemLineAdd_InventorySiteLocationRef_ListID.text = self.ItemLineAdd.InventorySiteLocationRef.ListID
                self.qbcom.ItemLineAdd_InventorySiteLocationRef_FullName = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'FullName')
                self.qbcom.ItemLineAdd_InventorySiteLocationRef_FullName.text = self.ItemLineAdd.InventorySiteLocationRef.FullName
            if self.ItemLineAdd.SerialNumber:
                self.qbcom.ItemLineAdd_SerialNumber = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'SerialNumber')
                self.qbcom.ItemLineAdd_SerialNumber.text = self.ItemLineAdd.SerialNumber
            elif self.ItemLineAdd.LotNumber:
                self.qbcom.ItemLineAdd_LotNumber = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'LotNumber')
                self.qbcom.ItemLineAdd_LotNumber.text = self.ItemLineAdd.LotNumber
            if self.ItemLineAdd.Desc:
                self.qbcom.ItemLineAdd_Desc = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'Desc')
                self.qbcom.ItemLineAdd_Desc.text = self.ItemLineAdd.Desc
            if self.ItemLineAdd.Quantity:
                self.qbcom.ItemLineAdd_Quantity = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'Quantity')
                self.qbcom.ItemLineAdd_Quantity.text = self.ItemLineAdd.Quantity
            if self.ItemLineAdd.UnitOfMeasure:
                self.qbcom.ItemLineAdd_UnitOfMeasure = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'UnitOfMeasure')
                self.qbcom.ItemLineAdd_UnitOfMeasure.text = self.ItemLineAdd.UnitOfMeasure
            if self.ItemLineAdd.Cost:
                self.qbcom.ItemLineAdd_Cost = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'Cost')
                self.qbcom.ItemLineAdd_Cost.text = self.ItemLineAdd.Cost
            if self.ItemLineAdd.Amount:
                self.qbcom.ItemLineAdd_Amount = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'Amount')
                self.qbcom.ItemLineAdd_Amount.text = self.ItemLineAdd.Amount
            if self.ItemLineAdd.CustomerRef.ListID or self.ItemLineAdd.CustomerRef.FullName:
                self.qbcom.ItemLineAdd_CustomerRef = ET.SubElement(self.qbcom.CheckAdd, 'CustomerRef')
                self.qbcom.ItemLineAdd_CustomerRef_ListID = ET.SubElement(self.qbcom.ItemLineAdd.CustomerRef, 'ListID')
                self.qbcom.ItemLineAdd_CustomerRef_ListID.text = self.ItemLineAdd.CustomerRef.ListID
                self.qbcom.ItemLineAdd_CustomerRef_FullName = ET.SubElement(self.qbcom.ItemLineAdd.CustomerRef, 'FullName')
                self.qbcom.ItemLineAdd_CustomerRef_FullName.text = self.ItemLineAdd.CustomerRef.FullName
            if self.ItemLineAdd.ClassRef.ListID or self.ItemLineAdd.ClassRef.FullName:
                self.qbcom.ItemLineAdd_ClassRef = ET.SubElement(self.qbcom.CheckAdd, 'ClassRef')
                self.qbcom.ItemLineAdd_ClassRef_ListID = ET.SubElement(self.qbcom.ItemLineAdd.ClassRef, 'ListID')
                self.qbcom.ItemLineAdd_ClassRef_ListID.text = self.ItemLineAdd.ClassRef.ListID
                self.qbcom.ItemLineAdd_ClassRef_FullName = ET.SubElement(self.qbcom.ItemLineAdd.ClassRef, 'FullName')
                self.qbcom.ItemLineAdd_ClassRef_FullName.text = self.ItemLineAdd.ClassRef.FullName
            if self.ItemLineAdd.BillableStatus:
                self.qbcom.ItemLineAdd_BillableStatus = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'BillableStatus')
                self.qbcom.ItemLineAdd_BillableStatus.text = self.ItemLineAdd.BillableStatus
            if self.ItemLineAdd.OverrideItemAccountRef.ListID or self.ItemLineAdd.OverrideItemAccountRef.FullName:
                self.qbcom.ItemLineAdd_OverrideItemAccountRef = ET.SubElement(self.qbcom.CheckAdd, 'OverrideItemAccountRef')
                self.qbcom.ItemLineAdd_OverrideItemAccountRef_ListID = ET.SubElement(self.qbcom.ItemLineAdd.OverrideItemAccountRef, 'ListID')
                self.qbcom.ItemLineAdd_OverrideItemAccountRef_ListID.text = self.ItemLineAdd.OverrideItemAccountRef.ListID
                self.qbcom.ItemLineAdd_OverrideItemAccountRef_FullName = ET.SubElement(self.qbcom.ItemLineAdd.OverrideItemAccountRef, 'FullName')
                self.qbcom.ItemLineAdd_OverrideItemAccountRef_FullName.text = self.ItemLineAdd.OverrideItemAccountRef.FullName
            if self.ItemLineAdd.SalesRepRef.ListID or self.ItemLineAdd.SalesRepRef.FullName:
                self.qbcom.ItemLineAdd_SalesRepRef = ET.SubElement(self.qbcom.CheckAdd, 'SalesRepRef')
                self.qbcom.ItemLineAdd_SalesRepRef_ListID = ET.SubElement(self.qbcom.ItemLineAdd.SalesRepRef, 'ListID')
                self.qbcom.ItemLineAdd_SalesRepRef_ListID.text = self.ItemLineAdd.SalesRepRef.ListID
                self.qbcom.ItemLineAdd_SalesRepRef_FullName = ET.SubElement(self.qbcom.ItemLineAdd.SalesRepRef, 'FullName')
                self.qbcom.ItemLineAdd_SalesRepRef_FullName.text = self.ItemLineAdd.SalesRepRef.FullName
            if self.ItemLineAdd.DataExt.ListID or self.ItemLineAdd.DataExt.FullName:
                self.qbcom.ItemLineAdd_DataExt = ET.SubElement(self.qbcom.CheckAdd, 'DataExt')
                self.qbcom.ItemLineAdd_DataExt_OwnerID = ET.SubElement(self.qbcom.ItemLineAdd.DataExt, 'OwnerID')
                self.qbcom.ItemLineAdd_DataExt_OwnerID.text = self.ItemLineAdd.DataExt.OwnerID
                self.qbcom.ItemLineAdd_DataExt_DataExtName = ET.SubElement(self.qbcom.ItemLineAdd.DataExt, 'DataExtName')
                self.qbcom.ItemLineAdd_DataExt_DataExtName.text = self.ItemLineAdd.DataExt.DataExtName
                self.qbcom.ItemLineAdd_DataExt_DataExtValue = ET.SubElement(self.qbcom.ItemLineAdd.DataExt, 'DataExtValue')
                self.qbcom.ItemLineAdd_DataExt_DataExtValue.text = self.ItemLineAdd.DataExt.DataExtValue
        elif (self.ItemGroupLineAdd.ItemGroupRef.ListID or
                self.ItemGroupLineAdd.ItemGroupRef.FullName or
                self.ItemGroupLineAdd.Quantity or
                self.ItemGroupLineAdd.UnitOfMeasure or
                self.ItemGroupLineAdd.InventorySiteRef.ListID or
                self.ItemGroupLineAdd.InventorySiteRef.FullName or
                self.ItemGroupLineAdd.InventorySiteLocationRef.ListID or
                self.ItemGroupLineAdd.InventorySiteLocationRef.FullName or
                self.ItemGroupLineAdd.DataExt.OwnerID or
                self.ItemGroupLineAdd.DataExt.DataExtName or
                self.ItemGroupLineAdd.DataExt.DataExtValue):
            self.qbcom.ItemGroupLineAdd = ET.SubElement(self.qbcom.CheckAdd, 'ItemGroupLineAdd')
            if self.ItemGroupLineAdd.ItemGroupRef.ListID or self.ItemGroupLineAdd.ItemGroupRef.FullName:
                self.qbcom.ItemGroupLineAdd_ItemGroupRef = ET.SubElement(self.qbcom.CheckAdd, 'ItemGroupRef')
                self.qbcom.ItemGroupLineAdd_ItemGroupRef_ListID = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'ListID')
                self.qbcom.ItemGroupLineAdd_ItemGroupRef_ListID.text = self.ItemGroupLineAdd.ItemGroupRef.ListID
                self.qbcom.ItemGroupLineAdd_ItemGroupRef_FullName = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'FullName')
                self.qbcom.ItemGroupLineAdd_ItemGroupRef_FullName.text = self.ItemGroupLineAdd.ItemGroupRef.FullName
            if self.ItemGroupLineAdd.Quantity:
                self.qbcom.ItemGroupLineAdd_Quantity = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'Quantity')
                self.qbcom.ItemGroupLineAdd_Quantity.text = self.ItemGroupLineAdd.Quantity
            if self.ItemGroupLineAdd.UnitOfMeasure:
                self.qbcom.ItemGroupLineAdd_UnitOfMeasure = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'UnitOfMeasure')
                self.qbcom.ItemGroupLineAdd_UnitOfMeasure.text = self.ItemGroupLineAdd.UnitOfMeasure
            if self.ItemGroupLineAdd.InventorySiteRef.ListID or self.ItemGroupLineAdd.InventorySiteRef.FullName:
                self.qbcom.ItemGroupLineAdd_InventorySiteRef = ET.SubElement(self.qbcom.CheckAdd, 'InventorySiteRef')
                self.qbcom.ItemGroupLineAdd_InventorySiteRef_ListID = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'ListID')
                self.qbcom.ItemGroupLineAdd_InventorySiteRef_ListID.text = self.ItemGroupLineAdd.InventorySiteRef.ListID
                self.qbcom.ItemGroupLineAdd_InventorySiteRef_FullName = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'FullName')
                self.qbcom.ItemGroupLineAdd_InventorySiteRef_FullName.text = self.ItemGroupLineAdd.InventorySiteRef.FullName
            if self.ItemGroupLineAdd.InventorySiteLocationRef.ListID or self.ItemGroupLineAdd.InventorySiteLocationRef.FullName:
                self.qbcom.ItemGroupLineAdd_InventorySiteLocationRef = ET.SubElement(self.qbcom.CheckAdd, 'InventorySiteLocationRef')
                self.qbcom.ItemGroupLineAdd_InventorySiteLocationRef_ListID = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'ListID')
                self.qbcom.ItemGroupLineAdd_InventorySiteLocationRef_ListID.text = self.ItemGroupLineAdd.InventorySiteLocationRef.ListID
                self.qbcom.ItemGroupLineAdd_InventorySiteLocationRef_FullName = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'FullName')
                self.qbcom.ItemGroupLineAdd_InventorySiteLocationRef_FullName.text = self.ItemGroupLineAdd.InventorySiteLocationRef.FullName
            if self.ItemGroupLineAdd.DataExt.ListID or self.ItemGroupLineAdd.DataExt.FullName:
                self.qbcom.ItemGroupLineAdd_DataExt = ET.SubElement(self.qbcom.CheckAdd, 'DataExt')
                self.qbcom.ItemGroupLineAdd_DataExt_OwnerID = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'OwnerID')
                self.qbcom.ItemGroupLineAdd_DataExt = ET.SubElement(self.qbcom.CheckAdd, 'DataExt')
                self.qbcom.ItemGroupLineAdd_DataExt_DataExtName = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'DataExtName')
                self.qbcom.ItemGroupLineAdd_DataExt = ET.SubElement(self.qbcom.CheckAdd, 'DataExt')
                self.qbcom.ItemGroupLineAdd_DataExt_DataExtValue = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'DataExtValue')
        if self.IncludeRetElement:
            for item in self.IncludeRetElemenet:
                self.qbcom.IncludeRetElement = ET.SubElement(self.qbcom.CheckAddRq, 'IncludeRetElement')
                self.qbcom.IncludeRetElement.text = item

    def set_CustomerAddRq_attributes(self):
        '''
        My IDE sure does hate me doing this, but it sure does work
        Any suggestions on a better way to do this???
        '''
        self.qbcom.QBXMLMsgsRq.set('onError', self.onError)
        self.qbcom.CustomerAddRq = ET.SubElement(self.qbcom.QBXMLMsgsRq, 'CustomerAddRq')
        self.qbcom.CustomerAdd = ET.SubElement(self.qbcom.CustomerAddRq, 'CustomerAdd')
        if self.Name:
            self.qbcom.Name = ET.SubElement(self.qbcom.CustomerAdd, 'Name')
            self.qbcom.Name.text = self.Name
        if self.RefNumber:
            self.qbcom.RefNumber = ET.SubElement(self.qbcom.CustomerAdd, 'RefNumber')
            self.qbcom.RefNumber.text = self.RefNumber
        if self.ClassRef.ListID or self.ClassRef.FullName:
            self.qbcom.ClassRef = ET.SubElement(self.qbcom.CustomerAdd, 'ClassRef')
            self.qbcom.ClassRef_ListID = ET.SubElement(self.qbcom.ClassRef, 'ListID')
            self.qbcom.ClassRef_ListID.text = self.ClassRef.ListID
            self.qbcom.ClassRef_FullName = ET.SubElement(self.qbcom.ClassRef, 'FullName')
            self.qbcom.ClassRef_FullName.text = self.ClassRef.FullName
        if self.ParentRef.ListID or self.ParentRef.FullName:
            self.qbcom.ParentRef = ET.SubElement(self.qbcom.CustomerAdd, 'ParentRef')
            self.qbcom.ParentRef_ = search_parameter()
            self.qbcom.ParentRef_.ListID = ET.SubElement(self.qbcom.ParentRef, 'ListID')
            self.qbcom.ParentRef_.ListID.text = self.ParentRef.ListID
            self.qbcom.ParentRef_.FullName = ET.SubElement(self.qbcom.ParentRef, 'FullName')
            self.qbcom.ParentRef_.FullName.text = self.ParentRef.FullName
        if self.CompanyName:
            self.qbcom.CompanyName = ET.SubElement(self.qbcom.CustomerAdd, 'CompanyName')
            self.qbcom.CompanyName.text = self.CompanyName
        if self.Salutation:
            self.qbcom.Salutation = ET.SubElement(self.qbcom.CustomerAdd, 'Salutation')
            self.qbcom.Salutation.text = self.Salutation
        if self.FirstName:
            self.qbcom.FirstName = ET.SubElement(self.qbcom.CustomerAdd, 'FirstName')
            self.qbcom.FirstName.text = self.FirstName
        if self.MiddleName:
            self.qbcom.MiddleName = ET.SubElement(self.qbcom.CustomerAdd, 'MiddleName')
            self.qbcom.MiddleName.text = self.MiddleName
        if self.LastName:
            self.qbcom.LastName = ET.SubElement(self.qbcom.CustomerAdd, 'LastName')
            self.qbcom.LastName.text = self.LastName
        if self.JobTitle:
            self.qbcom.JobTitle = ET.SubElement(self.qbcom.CustomerAdd, 'JobTitle')
            self.qbcom.JobTitle.text = self.JobTitle
        if (    self.BillAddress.Addr1 and
                self.BillAddress.Addr2 and
                self.BillAddress.Addr3 and
                self.BillAddress.City and
                self.BillAddress.State and
                self.BillAddress.PostalCode and
                self.BillAddress.Country and
                not self.BillAddress.Addr4 and
                not self.BillAddress.Addr5):
            self.qbcom.BillAddress = ET.SubElement(self.qbcom.CustomerAdd, 'BillAddress')
            self.qbcom.BillAddress_ = search_parameter()
            self.qbcom.BillAddress_.Addr1 = ET.SubElement(self.qbcom.BillAddress, 'Addr1')
            self.qbcom.BillAddress_.Addr1.text = self.BillAddress.Addr1
            self.qbcom.BillAddress_.Addr2 = ET.SubElement(self.qbcom.BillAddress, 'Addr2')
            self.qbcom.BillAddress_.Addr2.text = self.BillAddress.Addr2
            self.qbcom.BillAddress_.Addr3 = ET.SubElement(self.qbcom.BillAddress, 'Addr3')
            self.qbcom.BillAddress_.Addr3.text = self.BillAddress.Addr3
            self.qbcom.BillAddress_.City = ET.SubElement(self.qbcom.BillAddress, 'City')
            self.qbcom.BillAddress_.City.text = self.BillAddress.City
            self.qbcom.BillAddress_.State = ET.SubElement(self.qbcom.BillAddress, 'State')
            self.qbcom.BillAddress_.State.text = self.BillAddress.State
            self.qbcom.BillAddress_.PostalCode = ET.SubElement(self.qbcom.BillAddress, 'PostalCode')
            self.qbcom.BillAddress_.PostalCode.text = self.BillAddress.PostalCode
            if self.BillAddress.Country:
                self.qbcom.BillAddress_.Country = ET.SubElement(self.qbcom.BillAddress, 'Country')
                self.qbcom.BillAddress_.Country.text = self.BillAddress.Country
            if self.BillAddress.Note:
                self.qbcom.BillAddress_.Note = ET.SubElement(self.qbcom.BillAddress, 'Note')
                self.qbcom.BillAddress_.Note.text = self.BillAddress.Note
        if (    self.BillAddress.Addr1 and
                self.BillAddress.Addr2 and
                self.BillAddress.Addr3 and
                self.BillAddress.Addr4 and
                self.BillAddress.Addr5 and
                not self.BillAddress.City and
                not self.BillAddress.State and
                not self.BillAddress.PostalCode and
                not self.BillAddress.Country):
            self.qbcom.BillAddress_ = ET.SubElement(self.qbcom.CustomerAdd, 'BillAddress')
            self.qbcom.BillAddress_ = search_parameter()
            self.qbcom.BillAddress_.Addr1 = ET.SubElement(self.qbcom.BillAddress, 'Addr1')
            self.qbcom.BillAddress_.Addr1.text = self.BillAddress.Addr1
            self.qbcom.BillAddress_.Addr2 = ET.SubElement(self.qbcom.BillAddress, 'Addr2')
            self.qbcom.BillAddress_.Addr2.text = self.BillAddress.Addr2
            self.qbcom.BillAddress_.Addr3 = ET.SubElement(self.qbcom.BillAddress, 'Addr3')
            self.qbcom.BillAddress_.Addr3.text = self.BillAddress.Addr3
            self.qbcom.BillAddress_.Addr4 = ET.SubElement(self.qbcom.BillAddress, 'Addr4')
            self.qbcom.BillAddress_.Addr4.text = self.BillAddress.Addr4
            self.qbcom.BillAddress_.Addr5 = ET.SubElement(self.qbcom.BillAddress, 'Addr5')
            self.qbcom.BillAddress_.Addr5.text = self.BillAddress.Addr5
            if self.BillAddress.Note:
                self.qbcom.BillAddress_.Note = ET.SubElement(self.qbcom.BillAddress, 'Note')
                self.qbcom.BillAddress_.Note.text = self.BillAddress.Note
        if (    self.ShipAddress.Addr1 and
                self.ShipAddress.Addr2 and
                self.ShipAddress.Addr3 and
                self.ShipAddress.City and
                self.ShipAddress.State and
                self.ShipAddress.PostalCode and
                not self.ShipAddress.Addr4 and
                not self.ShipAddress.Addr5):
            self.qbcom.ShipAddress = ET.SubElement(self.qbcom.CustomerAdd, 'ShipAddress')
            self.qbcom.ShipAddress_ = search_parameter()
            self.qbcom.ShipAddress_.Addr1 = ET.SubElement(self.qbcom.ShipAddress, 'Addr1')
            self.qbcom.ShipAddress_.Addr1.text = self.ShipAddress.Addr1
            self.qbcom.ShipAddress_.Addr2 = ET.SubElement(self.qbcom.ShipAddress, 'Addr2')
            self.qbcom.ShipAddress_.Addr2.text = self.ShipAddress.Addr2
            self.qbcom.ShipAddress_.Addr3 = ET.SubElement(self.qbcom.ShipAddress, 'Addr3')
            self.qbcom.ShipAddress_.Addr3.text = self.ShipAddress.Addr3
            self.qbcom.ShipAddress_.City = ET.SubElement(self.qbcom.ShipAddress, 'City')
            self.qbcom.ShipAddress_.City.text = self.ShipAddress.City
            self.qbcom.ShipAddress_.State = ET.SubElement(self.qbcom.ShipAddress, 'State')
            self.qbcom.ShipAddress_.State.text = self.ShipAddress.State
            self.qbcom.ShipAddress_.PostalCode = ET.SubElement(self.qbcom.ShipAddress, 'PostalCode')
            self.qbcom.ShipAddress_.PostalCode.text = self.ShipAddress.PostalCode
            if self.ShipAddress.Country:
                self.qbcom.ShipAddress_.Country = ET.SubElement(self.qbcom.ShipAddress, 'Country')
                self.qbcom.ShipAddress_.Country.text = self.ShipAddress.Country
            if self.ShipAddress.Note:
                self.qbcom.ShipAddress_.Note = ET.SubElement(self.qbcom.ShipAddress, 'Note')
                self.qbcom.ShipAddress_.Note.text = self.ShipAddress.Note
        if (    self.ShipAddress.Addr1 and
                self.ShipAddress.Addr2 and
                self.ShipAddress.Addr3 and
                self.ShipAddress.Addr4 and
                self.ShipAddress.Addr5 and
                not self.ShipAddress.City and
                not self.ShipAddress.State and
                not self.ShipAddress.PostalCode and
                not self.ShipAddress.Country):
            self.qbcom.ShipAddress = ET.SubElement(self.qbcom.CustomerAdd, 'ShipAddress')
            self.qbcom.ShipAddress_ = search_parameter()
            self.qbcom.ShipAddress_.Addr1 = ET.SubElement(self.qbcom.ShipAddress, 'Addr1')
            self.qbcom.ShipAddress_.Addr1.text = self.ShipAddress.Addr1
            self.qbcom.ShipAddress_.Addr2 = ET.SubElement(self.qbcom.ShipAddress, 'Addr2')
            self.qbcom.ShipAddress_.Addr2.text = self.ShipAddress.Addr2
            self.qbcom.ShipAddress_.Addr3 = ET.SubElement(self.qbcom.ShipAddress, 'Addr3')
            self.qbcom.ShipAddress_.Addr3.text = self.ShipAddress.Addr3
            self.qbcom.ShipAddress_.Addr4 = ET.SubElement(self.qbcom.ShipAddress, 'Addr4')
            self.qbcom.ShipAddress_.Addr4.text = self.ShipAddress.Addr4
            self.qbcom.ShipAddress_.Addr5 = ET.SubElement(self.qbcom.ShipAddress, 'Addr5')
            self.qbcom.ShipAddress_.Addr5.text = self.ShipAddress.Addr5
            if self.ShipAddress.Note:
                self.qbcom.ShipAddress_.Note = ET.SubElement(self.qbcom.ShipAddress, 'Note')
                self.qbcom.ShipAddress_.Note.text = self.ShipAddress.Note
        if (    self.ShipToAddress.Addr1 and
                self.ShipToAddress.Addr2 and
                self.ShipToAddress.Addr3 and
                self.ShipToAddress.City and
                self.ShipToAddress.State and
                self.ShipToAddress.PostalCode and
                not self.ShipToAddress.Addr4 and
                not self.ShipToAddress.Addr5):
            self.qbcom.ShipToAddress = ET.SubElement(self.qbcom.CustomerAdd, 'ShipToAddress')
            self.qbcom.ShipToAddress_ = search_parameter()
            self.qbcom.ShipToAddress_.Addr1 = ET.SubElement(self.qbcom.ShipToAddress, 'Addr1')
            self.qbcom.ShipToAddress_.Addr1.text = self.ShipToAddress.Addr1
            self.qbcom.ShipToAddress_.Addr2 = ET.SubElement(self.qbcom.ShipToAddress, 'Addr2')
            self.qbcom.ShipToAddress_.Addr2.text = self.ShipToAddress.Addr2
            self.qbcom.ShipToAddress_.Addr3 = ET.SubElement(self.qbcom.ShipToAddress, 'Addr3')
            self.qbcom.ShipToAddress_.Addr3.text = self.ShipToAddress.Addr3
            self.qbcom.ShipToAddress_.City = ET.SubElement(self.qbcom.ShipToAddress, 'City')
            self.qbcom.ShipToAddress_.City.text = self.ShipToAddress.City
            self.qbcom.ShipToAddress_.State = ET.SubElement(self.qbcom.ShipToAddress, 'State')
            self.qbcom.ShipToAddress_.State.text = self.ShipToAddress.State
            self.qbcom.ShipToAddress_.PostalCode = ET.SubElement(self.qbcom.ShipToAddress, 'PostalCode')
            self.qbcom.ShipToAddress_.PostalCode.text = self.ShipToAddress.PostalCode
            if self.ShipToAddress.Country:
                self.qbcom.ShipToAddress_.Country = ET.SubElement(self.qbcom.ShipToAddress, 'Country')
                self.qbcom.ShipToAddress_.Country.text = self.ShipToAddress.Country
            if self.ShipToAddress.Note:
                self.qbcom.ShipToAddress_.Note = ET.SubElement(self.qbcom.ShipToAddress, 'Note')
                self.qbcom.ShipToAddress_.Note.text = self.ShipToAddress.Note
            if self.ShipToAddress.DefaultShipTo:
                self.qbcom.ShipToAddress_.DefaultShipTo = ET.SubElement(self.qbcom.ShipToAddress, 'DefaultShipTo')
                self.qbcom.ShipToAddress_.DefaultShipTo.text = self.ShipToAddress.Note
        if (    self.ShipToAddress.Addr1 and
                self.ShipToAddress.Addr2 and
                self.ShipToAddress.Addr3 and
                self.ShipToAddress.Addr4 and
                self.ShipToAddress.Addr5 and
                not self.ShipToAddress.City and
                not self.ShipToAddress.State and
                not self.ShipToAddress.PostalCode and
                not self.ShipToAddress.Country):
            self.qbcom.ShipToAddress = ET.SubElement(self.qbcom.CustomerAdd, 'ShipToAddress')
            self.qbcom.ShipToAddress_ = search_parameter()
            self.qbcom.ShipToAddress_.Addr1 = ET.SubElement(self.qbcom.ShipToAddress, 'Addr1')
            self.qbcom.ShipToAddress_.Addr1.text = self.ShipToAddress.Addr1
            self.qbcom.ShipToAddress_.Addr2 = ET.SubElement(self.qbcom.ShipToAddress, 'Addr2')
            self.qbcom.ShipToAddress_.Addr2.text = self.ShipToAddress.Addr2
            self.qbcom.ShipToAddress_.Addr3 = ET.SubElement(self.qbcom.ShipToAddress, 'Addr3')
            self.qbcom.ShipToAddress_.Addr3.text = self.ShipToAddress.Addr3
            self.qbcom.ShipToAddress_.Addr4 = ET.SubElement(self.qbcom.ShipToAddress, 'Addr4')
            self.qbcom.ShipToAddress_.Addr4.text = self.ShipToAddress.Addr4
            self.qbcom.ShipToAddress_.Addr5 = ET.SubElement(self.qbcom.ShipToAddress, 'Addr5')
            self.qbcom.ShipToAddress_.Addr5.text = self.ShipToAddress.Addr5
            if self.ShipToAddress.Note:
                self.qbcom.ShipToAddress_.Note = ET.SubElement(self.qbcom.ShipToAddress, 'Note')
                self.qbcom.ShipToAddress_.Note.text = self.ShipToAddress.Note
            if self.ShipToAddress.DefaultShipTo:
                self.qbcom.ShipToAddress_.DefaultShipTo = ET.SubElement(self.qbcom.ShipToAddress, 'DefaultShipTo')
                self.qbcom.ShipToAddress_.DefaultShipTo.text = self.ShipToAddress.DefaultShipTo
        if self.Phone:
            self.qbcom.Phone = ET.SubElement(self.qbcom.CustomerAdd, 'Phone')
            self.qbcom.Phone.text = self.Phone
        if self.AltPhone:
            self.qbcom.AltPhone = ET.SubElement(self.qbcom.CustomerAdd, 'AltPhone')
            self.qbcom.AltPhone.text = self.AltPhone
        if self.Fax:
            self.qbcom.Fax = ET.SubElement(self.qbcom.CustomerAdd, 'Fax')
            self.qbcom.Fax.text = self.Fax
        if self.Email:
            self.qbcom.Email = ET.SubElement(self.qbcom.CustomerAdd, 'Email')
            self.qbcom.Email.text = self.Email
        if self.Cc:
            self.qbcom.Cc = ET.SubElement(self.qbcom.CustomerAdd, 'Cc')
            self.qbcom.Cc.text = self.Cc
        if self.Contact:
            self.qbcom.Contact = ET.SubElement(self.qbcom.CustomerAdd, 'Contact')
            self.qbcom.Contact.text = self.Contact
        if self.AltContact:
            self.qbcom.AltContact = ET.SubElement(self.qbcom.CustomerAdd, 'AltContact')
            self.qbcom.AltContact.text = self.AltContact
        if self.AdditionalContactRef.ContactName or self.AdditionalContactRef.ContactValue:
            self.qbcom.AdditionalContactRef = ET.SubElement(self.qbcom.CustomerAdd, 'AdditionalContactRef')
            self.qbcom.AdditionalContactRef_ = search_parameter()
            self.qbcom.AdditionalContactRef_.ContactName = ET.SubElement(self.qbcom.AdditionalContactRef, 'ContactName')
            self.qbcom.AdditionalContactRef_.ContactName.text = self.AdditionalContactRef.ContactName
            self.qbcom.AdditionalContactRef_.ContactValue = ET.SubElement(self.qbcom.AdditionalContactRef, 'ContactValue')
            self.qbcom.AdditionalContactRef_.ContactValue.text = self.AdditionalContactRef.ContactValue
        if (self.Contacts.Salutation or
                self.Contacts.FirstName or
                self.Contacts.MiddleName or
                self.Contacts.LastName or
                self.Contacts.JobTitle):
            self.qbcom.Contacts = ET.SubElement(self.qbcom.CustomerAdd, 'Contacts')
            self.qbcom.Contacts_ = search_parameter()
            self.qbcom.Contacts_.Salutation = ET.SubElement(self.qbcom.Contacts, 'Salutation')
            self.qbcom.Contacts_.Salutation.text = self.Contacts.Salutation
            self.qbcom.Contacts_.FirstName = ET.SubElement(self.qbcom.Contacts, 'FirstName')
            self.qbcom.Contacts_.FirstName.text = self.Contacts.FirstName
            self.qbcom.Contacts_.MiddleName = ET.SubElement(self.qbcom.Contacts, 'MiddleName')
            self.qbcom.Contacts_.MiddleName.text = self.Contacts.MiddleName
            self.qbcom.Contacts_.LastName = ET.SubElement(self.qbcom.Contacts, 'LastName')
            self.qbcom.Contacts_.LastName.text = self.Contacts.LastName
            self.qbcom.Contacts_.JobTitle = ET.SubElement(self.qbcom.Contacts, 'JobTitle')
            self.qbcom.Contacts_.JobTitle.text = self.Contacts.JobTitle
            if self.Contacts.AdditionalContactRef.ContactName or self.Contacts.AdditionalContactRef.ContactValue:
                self.qbcom.Contacts_.AdditionalContactRef = ET.SubElement(self.qbcom.Contacts, 'AdditionalContactRef')
                self.qbcom.Contacts_.AdditionalContactRef_ = search_parameter()
                self.qbcom.Contacts_.AdditionalContactRef_.ContactName = ET.SubElement(self.qbcom.Contacts.AdditionalContactRef, 'ContactName')
                self.qbcom.Contacts_.AdditionalContactRef_.ContactName.text = self.Contacts.AdditionalContactRef.ContactName
                self.qbcom.Contacts_.AdditionalContactRef_.ContactValue = ET.SubElement(self.qbcom.Contacts.AdditionalContactRef, 'ContactValue')
                self.qbcom.Contacts_.AdditionalContactRef_.ContactValue.text = self.Contacts.AdditionalContactRef.ContactValue
        if self.CustomerTypeRef.ListID or self.CustomerTypeRef.FullName:
            self.qbcom.CustomerTypeRef = ET.SubElement(self.qbcom.CustomerAdd, 'CustomerTypeRef')
            self.qbcom.CustomerTypeRef_ = search_parameter()
            self.qbcom.CustomerTypeRef_.ListID = ET.SubElement(self.qbcom.CustomerTypeRef, 'ListID')
            self.qbcom.CustomerTypeRef_.ListID.text = self.CustomerTypeRef.ListID
            self.qbcom.CustomerTypeRef_.FullName = ET.SubElement(self.qbcom.CustomerTypeRef, 'FullName')
            self.qbcom.CustomerTypeRef_.FullName.text = self.CustomerTypeRef.FullName
        if self.TermsRef.ListID or self.TermsRef.FullName:
            self.qbcom.TermsRef = ET.SubElement(self.qbcom.CustomerAdd, 'TermsRef')
            self.qbcom.TermsRef_ = search_parameter()
            self.qbcom.TermsRef_.ListID = ET.SubElement(self.qbcom.TermsRef, 'ListID')
            self.qbcom.TermsRef_.ListID.text = self.TermsRef.ListID
            self.qbcom.TermsRef_.FullName = ET.SubElement(self.qbcom.TermsRef, 'FullName')
            self.qbcom.TermsRef_.FullName.text = self.TermsRef.FullName
        if self.SalesRepRef.ListID or self.SalesRepRef.FullName:
            self.qbcom.SalesRepRef = ET.SubElement(self.qbcom.CustomerAdd, 'SalesRepRef')
            self.qbcom.SalesRepRef_ = search_parameter()
            self.qbcom.SalesRepRef_.ListID = ET.SubElement(self.qbcom.SalesRepRef, 'ListID')
            self.qbcom.SalesRepRef_.ListID.text = self.SalesRepRef.ListID
            self.qbcom.SalesRepRef_.FullName = ET.SubElement(self.qbcom.SalesRepRef, 'FullName')
            self.qbcom.SalesRepRef_.FullName.text = self.SalesRepRef.FullName
        if self.OpenBalance:
            self.qbcom.OpenBalance = ET.SubElement(self.qbcom.CustomerAdd, 'OpenBalance')
            self.qbcom.OpenBalance.text = self.OpenBalance
        if self.OpenBalanceDate:
            self.qbcom.OpenBalanceDate = ET.SubElement(self.qbcom.CustomerAdd, 'OpenBalanceDate')
            self.qbcom.OpenBalanceDate.text = self.OpenBalanceDate
        if self.SalesTaxCodeRef.ListID or self.SalesTaxCodeRef.FullName:
            self.qbcom.SalesTaxCodeRef = ET.SubElement(self.qbcom.CustomerAdd, 'SalesTaxCodeRef')
            self.qbcom.SalesTaxCodeRef_ = search_parameter()
            self.qbcom.SalesTaxCodeRef_.ListID = ET.SubElement(self.qbcom.SalesTaxCodeRef, 'ListID')
            self.qbcom.SalesTaxCodeRef_.ListID.text = self.SalesTaxCodeRef.ListID
            self.qbcom.SalesTaxCodeRef_.FullName = ET.SubElement(self.qbcom.SalesTaxCodeRef, 'FullName')
            self.qbcom.SalesTaxCodeRef_.FullName.text = self.SalesTaxCodeRef.FullName
        if self.ItemSalesTaxRef.ListID or self.ItemSalesTaxRef.FullName:
            self.qbcom.ItemSalesTaxRef = ET.SubElement(self.qbcom.CustomerAdd, 'ItemSalesTaxRef')
            self.qbcom.ItemSalesTaxRef_ = search_parameter()
            self.qbcom.ItemSalesTaxRef_.ListID = ET.SubElement(self.qbcom.ItemSalesTaxRef, 'ListID')
            self.qbcom.ItemSalesTaxRef_.ListID.text = self.ItemSalesTaxRef.ListID
            self.qbcom.ItemSalesTaxRef_.FullName = ET.SubElement(self.qbcom.ItemSalesTaxRef, 'FullName')
            self.qbcom.ItemSalesTaxRef_.FullName.text = self.ItemSalesTaxRef.FullName
        if self.ResaleNumber:
            self.qbcom.ResaleNumber = ET.SubElement(self.qbcom.CustomerAdd, 'ResaleNumber')
            self.qbcom.ResaleNumber.text = self.ResaleNumber
        if self.AccountNumber:
            self.qbcom.AccountNumber = ET.SubElement(self.qbcom.CustomerAdd, 'AccountNumber')
            self.qbcom.AccountNumber.text = self.AccountNumber
        if self.CreditLimit:
            self.qbcom.CreditLimit = ET.SubElement(self.qbcom.CustomerAdd, 'CreditLimit')
            self.qbcom.CreditLimit.text = self.CreditLimit
        if self.PreferredPaymentMethodRef.ListID or self.PreferredPaymentMethodRef.FullName:
            self.qbcom.PreferredPaymentMethodRef = ET.SubElement(self.qbcom.CustomerAdd, 'PreferredPaymentMethodRef')
            self.qbcom.PreferredPaymentMethodRef_ = search_parameter()
            self.qbcom.PreferredPaymentMethodRef_.ListID = ET.SubElement(self.qbcom.PreferredPaymentMethodRef, 'ListID')
            self.qbcom.PreferredPaymentMethodRef_.ListID.text = self.PreferredPaymentMethodRef.ListID
            self.qbcom.PreferredPaymentMethodRef_.FullName = ET.SubElement(self.qbcom.PreferredPaymentMethodRef, 'FullName')
            self.qbcom.PreferredPaymentMethodRef_.FullName.text = self.PreferredPaymentMethodRef.FullName
        if self.CreditCardInfo.CreditCardNumber or self.CreditCardInfo.ExpirationMonth:
            self.qbcom.CreditCardInfo = ET.SubElement(self.qbcom.CustomerAdd, 'CreditCardInfo')
            self.qbcom.CreditCardInfo_ = search_parameter()
            self.qbcom.CreditCardInfo_.CreditCardNumber = ET.SubElement(self.qbcom.CreditCardInfo, 'CreditCardNumber')
            self.qbcom.CreditCardInfo_.CreditCardNumber.text = self.CreditCardInfo.CreditCardNumber
            self.qbcom.CreditCardInfo_.ExpirationMonth = ET.SubElement(self.qbcom.CreditCardInfo, 'ExpirationMonth')
            self.qbcom.CreditCardInfo_.ExpirationMonth.text = self.CreditCardInfo.ExpirationMonth
            self.qbcom.CreditCardInfo_.ExpirationYear = ET.SubElement(self.qbcom.CreditCardInfo, 'ExpirationYear')
            self.qbcom.CreditCardInfo_.ExpirationYear.text = self.CreditCardInfo.ExpirationYear
            self.qbcom.CreditCardInfo_.NameOnCard = ET.SubElement(self.qbcom.CreditCardInfo, 'NameOnCard')
            self.qbcom.CreditCardInfo_.NameOnCard.text = self.CreditCardInfo.NameOnCard
            self.qbcom.CreditCardInfo_.CreditCardAddress = ET.SubElement(self.qbcom.CreditCardInfo, 'CreditCardAddress')
            self.qbcom.CreditCardInfo_.CreditCardAddress.text = self.CreditCardInfo.CreditCardAddress
            self.qbcom.CreditCardInfo_.CreditCardPostalCode = ET.SubElement(self.qbcom.CreditCardInfo, 'CreditCardPostalCode')
            self.qbcom.CreditCardInfo_.CreditCardPostalCode.text = self.CreditCardInfo.CreditCardPostalCode
        if self.JobStatus:
            self.qbcom.JobStatus = ET.SubElement(self.qbcom.CustomerAdd, 'JobStatus')
            self.qbcom.JobStatus.text = self.JobStatus
        if self.JobStartDate:
            self.qbcom.JobStartDate = ET.SubElement(self.qbcom.CustomerAdd, 'JobStartDate')
            self.qbcom.JobStartDate.text = self.JobStartDate
        if self.JobProjectedEndDate:
            self.qbcom.JobProjectedEndDate = ET.SubElement(self.qbcom.CustomerAdd, 'JobProjectedEndDate')
            self.qbcom.JobProjectedEndDate.text = self.JobProjectedEndDate
        if self.JobEndDate:
            self.qbcom.JobEndDate = ET.SubElement(self.qbcom.CustomerAdd, 'JobEndDate')
            self.qbcom.JobEndDate.text = self.JobEndDate
        if self.JobDesc:
            self.qbcom.JobDesc = ET.SubElement(self.qbcom.CustomerAdd, 'JobDesc')
            self.qbcom.JobDesc.text = self.JobDesc
            self.qbcom.JobTypeRef = ET.SubElement(self.qbcom.CustomerAdd, 'JobTypeRef')
            self.qbcom.JobTypeRef_ = search_parameter()
            self.qbcom.JobTypeRef_.ListID = ET.SubElement(self.qbcom.JobTypeRef, 'ListID')
            self.qbcom.JobTypeRef_.ListID.text = self.JobTypeRef.ListID
            self.qbcom.JobTypeRef_.FullName = ET.SubElement(self.qbcom.JobTypeRef, 'FullName')
            self.qbcom.JobTypeRef_.FullName.text = self.JobTypeRef.FullName
        if self.Notes:
            self.qbcom.Notes = ET.SubElement(self.qbcom.CustomerAdd, 'Notes')
            self.qbcom.Notes.text = self.Notes
        if self.AdditionalNotes.Notes:
            self.qbcom.AdditionalNotes = ET.SubElement(self.qbcom.CustomerAdd, 'AdditionalNotes')
            self.qbcom.AdditionalNotes_ = search_parameter()
            self.qbcom.AdditionalNotes_.Notes = ET.SubElement(self.qbcom.AdditionalNotes, 'Notes')
            self.qbcom.AdditionalNotes_.Notes.text = self.AdditionalNotes.Notes
        if self.PreferredDeliveryMethod:
            self.qbcom.PreferredDeliveryMethod = ET.SubElement(self.qbcom.CustomerAdd, 'PreferredDeliveryMethod')
            self.qbcom.PreferredDeliveryMethod.text = self.PreferredDeliveryMethod
        if self.PriceLevelRef.ListID or self.PriceLevelRef.FullName:
            self.qbcom.PriceLevelRef = ET.SubElement(self.qbcom.CustomerAdd, 'PriceLevelRef')
            self.qbcom.PriceLevelRef_ = search_parameter()
            self.qbcom.PriceLevelRef_.ListID = ET.SubElement(self.qbcom.PriceLevelRef, 'ListID')
            self.qbcom.PriceLevelRef_.ListID.text = self.PriceLevelRef.ListID
            self.qbcom.PriceLevelRef_.FullName = ET.SubElement(self.qbcom.PriceLevelRef, 'FullName')
            self.qbcom.PriceLevelRef_.FullName.text = self.PriceLevelRef.FullName
        if self.ExternalGUID:
            self.qbcom.ExternalGUID = ET.SubElement(self.qbcom.CustomerAdd, 'ExternalGUID')
            self.qbcom.ExternalGUID.text = self.ExternalGUID
        if self.CurrencyRef.ListID or self.CurrencyRef.FullName:
            self.qbcom.CurrencyRef = ET.SubElement(self.qbcom.CustomerAdd, 'CurrencyRef')
            self.qbcom.CurrencyRef_ = search_parameter()
            self.qbcom.CurrencyRef_.ListID = ET.SubElement(self.qbcom.CurrencyRef, 'ListID')
            self.qbcom.CurrencyRef_.ListID.text = self.CurrencyRef.ListID
            self.qbcom.CurrencyRef_.FullName = ET.SubElement(self.qbcom.CurrencyRef, 'FullName')
            self.qbcom.CurrencyRef_.FullName.text = self.CurrencyRef.FullName
        if self.IncludeRetElement:
            for item in self.IncludeRetElemenet:
                self.qbcom.IncludeRetElement = ET.SubElement(self.qbcom.CustomerAddRq, 'IncludeRetElement')
                self.qbcom.IncludeRetElement.text = item
