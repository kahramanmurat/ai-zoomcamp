# Testing Guide for Django Todo Application

This guide will help you test all the features of the Todo application.

## Quick Start Testing

### 1. Start the Development Server

```bash
python3 manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`

### 2. Open in Browser

Navigate to: **http://127.0.0.1:8000/**

---

## Feature Testing Checklist

### ✅ Basic CRUD Operations

#### Create Todo
- [ ] Click "Create New Todo" button
- [ ] Fill in title (required field)
- [ ] Add description (optional)
- [ ] Set a due date and time (optional)
- [ ] Click "Save Todo"
- [ ] Verify success message appears
- [ ] Verify todo appears in the list

**Test Cases:**
- Create todo with all fields filled
- Create todo with only title (minimal)
- Create todo with past due date (should show as overdue)
- Create todo with future due date

#### Read/View Todos
- [ ] Verify all todos are displayed on homepage
- [ ] Check that task counts are accurate:
  - Total Tasks count
  - Resolved count
  - Pending count
- [ ] Verify datetime display in upper right corner updates every second
- [ ] Test both Grid and List views:
  - Click "Grid" button
  - Click "List" button
  - Verify todos display correctly in both views

#### Edit Todo
- [ ] Click "Edit" button on any todo
- [ ] Modify the title
- [ ] Update the description
- [ ] Change the due date
- [ ] Click "Save Todo"
- [ ] Verify changes are saved
- [ ] Verify success message appears

#### Delete Todo
- [ ] Click "Delete" button on a todo
- [ ] Verify confirmation page appears
- [ ] Click "Yes, Delete"
- [ ] Verify todo is removed from list
- [ ] Verify success message appears
- [ ] Verify task counts update correctly

#### Mark as Resolved
- [ ] Click "Resolve" button on a pending todo
- [ ] Verify todo is marked as resolved (grayed out, badge shows "Resolved")
- [ ] Verify success message appears
- [ ] Verify resolved count increases
- [ ] Verify pending count decreases
- [ ] Click "Unresolve" button
- [ ] Verify todo returns to pending status

---

### ✅ Filtering Features

#### Filter by Status
- [ ] Click "All" filter - verify all todos shown
- [ ] Click "Pending" filter - verify only unresolved todos shown
- [ ] Click "Resolved" filter - verify only completed todos shown
- [ ] Click "Overdue" filter - verify only overdue todos shown
- [ ] Test filters work in both Grid and List views

**Test Overdue Filter:**
1. Create a todo with a past due date
2. Ensure it's not marked as resolved
3. Click "Overdue" filter
4. Verify it appears in the list
5. Mark it as resolved
6. Click "Overdue" filter again - it should not appear

---

### ✅ View Modes

#### Grid View
- [ ] Verify todos display in card grid layout
- [ ] Verify all todo information is visible (title, description, dates)
- [ ] Verify action buttons (Resolve, Edit, Delete) are present
- [ ] Test on different screen sizes (responsive)

#### List View
- [ ] Switch to List view
- [ ] Verify todos display in compact list format
- [ ] Verify all information is visible
- [ ] Verify action buttons work correctly
- [ ] Test scrolling with many todos

#### View Persistence
- [ ] Switch to List view
- [ ] Apply a filter (e.g., "Pending")
- [ ] Verify you remain in List view
- [ ] Switch to Grid view
- [ ] Verify you remain in Grid view when filtering

---

### ✅ Statistics Display

#### Task Counts
- [ ] Create 5 todos total
- [ ] Mark 2 as resolved
- [ ] Create 1 overdue todo (past due date, not resolved)
- [ ] Verify all 4 stat cards show:
  - Total Tasks: 5
  - Resolved: 2
  - Pending: 3
  - Overdue: 1
- [ ] Delete 1 todo
- [ ] Verify counts update correctly
- [ ] Mark overdue todo as resolved
- [ ] Verify Overdue count decreases to 0
- [ ] Verify Resolved count increases

---

### ✅ UI/UX Features

#### Facebook Blue Theme
- [ ] Verify all primary buttons are Facebook blue
- [ ] Verify hover effects on buttons
- [ ] Verify background gradient uses Facebook blue tones
- [ ] Verify consistent color scheme throughout

#### Datetime Display
- [ ] Verify current date and time appears in upper right corner
- [ ] Wait a few seconds and verify it updates
- [ ] Verify format: "Month Day, Year, HH:MM:SS"

#### Responsive Design
- [ ] Resize browser window
- [ ] Test on mobile viewport (F12 → Toggle device toolbar)
- [ ] Verify todos adapt to screen size
- [ ] Verify datetime display is visible on all sizes

---

### ✅ Error Handling

#### Form Validation
- [ ] Try to create todo without title - should show error
- [ ] Try to submit empty form - should prevent submission
- [ ] Verify error messages display correctly

#### Empty States
- [ ] Delete all todos
- [ ] Verify "No todos found" message appears
- [ ] Verify stats show all zeros
- [ ] Verify "Create Todo" button is prominent

---

## Test Data Setup

### Quick Test Data Creation

You can create test data via:

1. **Admin Panel** (if you created a superuser):
   - Go to http://127.0.0.1:8000/admin/
   - Login with superuser credentials
   - Add todos from admin interface

2. **Via Web Interface**:
   - Manually create todos through the UI
   - Create at least 5-10 todos with different statuses

3. **Django Shell** (for bulk creation):
   ```bash
   python3 manage.py shell
   ```
   Then run:
   ```python
   from todos.models import Todo
   from django.utils import timezone
   from datetime import timedelta
   
   # Create some test todos
   Todo.objects.create(title="Test Todo 1", description="This is a test", is_resolved=False)
   Todo.objects.create(title="Test Todo 2", description="Another test", is_resolved=True)
   Todo.objects.create(title="Overdue Todo", due_date=timezone.now() - timedelta(days=1), is_resolved=False)
   Todo.objects.create(title="Future Todo", due_date=timezone.now() + timedelta(days=7), is_resolved=False)
   ```

---

## Browser Testing

Test in multiple browsers:
- [ ] Chrome/Edge
- [ ] Firefox
- [ ] Safari
- [ ] Mobile browser (if testing on mobile)

---

## Performance Testing

- [ ] Create 50+ todos
- [ ] Verify page loads quickly
- [ ] Test filtering with many todos
- [ ] Test switching between views
- [ ] Check browser console for errors (F12)

---

## Automated Testing (Optional)

You can also create automated tests. See the `tests.py` file section below for examples.

---

## Common Issues and Solutions

### Server won't start
- Check if port 8000 is already in use: `lsof -i :8000`
- Use different port: `python3 manage.py runserver 8001`

### Database errors
- Run migrations: `python3 manage.py migrate`

### Static files not loading
- Collect static files: `python3 manage.py collectstatic` (if using production mode)

### Datetime not updating
- Check browser console for JavaScript errors
- Ensure JavaScript is enabled

---

## Testing Workflow Example

1. **Initial Setup**
   ```
   python3 manage.py runserver
   ```

2. **Create Test Data**
   - Create 3 pending todos
   - Create 2 resolved todos
   - Create 1 overdue todo (past due date, not resolved)

3. **Test Statistics**
   - Verify: Total=6, Resolved=2, Pending=4

4. **Test Views**
   - Switch between Grid and List views
   - Verify all todos visible in both

5. **Test Filtering**
   - Filter by All → should show 6
   - Filter by Pending → should show 4
   - Filter by Resolved → should show 2
   - Filter by Overdue → should show 1

6. **Test CRUD**
   - Edit one todo
   - Delete one todo
   - Mark one as resolved
   - Verify counts update

7. **Test UI**
   - Verify Facebook blue theme
   - Verify datetime updates
   - Test responsive design

---

Happy Testing! 🎉

